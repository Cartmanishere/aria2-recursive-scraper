import requests
from bs4 import BeautifulSoup
import os
import urllib.parse as urp
import sys

banned = ["Parent Directory", "../", ".."]

def get_domain(link):
	return '{uri.scheme}://{uri.netloc}'.format(uri=urp.urlparse(link))

def assure_path_exists(path):
        if not os.path.exists(path):
                os.makedirs(path)

def recur(url, currentdir):
	root = get_domain(url)
	visited = set()
	r = requests.get(url)
	print("Get request to", url)
	visited.add(url)
	soup = BeautifulSoup(r.content, "lxml")
	i=0
	ite = soup.find_all("a")

	try:
		ite.pop(0)
	except Exception as e:
		'''
		When there is no link on page. Generally 404 or 403 page on nginx.
		'''
		pass


	assure_path_exists(urp.unquote(currentdir))
	file = open(urp.unquote(currentdir)+"links.txt", "w")

	for link in ite:
		if link.get("href")[0] == '/':
			temp_url = root + link.get("href")
		else:
			temp_url = url + link.get("href")

		if temp_url not in visited  and link.get("href") != '/':
			#print(temp_url)
			if link.get("href")[-1] != '/':
				if link.get("href")[0] == '/':
					file.write(root+link.get("href")+"\n")
				else:
					file.write(url+link.get("href")+"\n")
				print(link.get("href")+" <----- Scraped")

			else:
				if link.text not in banned and link.get("href")[-1] =='/':
					if link.get("href")[0] == '/': 
						po = root + link.get("href")
						temp = currentdir + link.get("href").split("/")[-2]
					else:
						po = url + link.get("href")
						temp = currentdir + link.get("href")

					recur(po, temp)

	file.close()

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("\n\nEnter URL to SCRAPE as COMMAND LINE ARGUMENT\n\n")
	else:
		recur(sys.argv[1], os.getcwd()+"/")
