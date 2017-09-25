import requests
from bs4 import BeautifulSoup
import os
import urllib.parse as urp
import sys

def assure_path_exists(path):
        if not os.path.exists(path):
                os.makedirs(path)

def recur(url, currentdir):
	visited = set()
	r = requests.get(url)
	print("Get request to", url)
	visited.add(url)
	soup = BeautifulSoup(r.content, "lxml")
	i=0
	ite = soup.find_all("a")
	ite.pop(0)
	assure_path_exists(urp.unquote(currentdir))
	file = open(urp.unquote(currentdir)+"links.txt", "w")

	for link in ite:
		temp_url = url + link.get("href")
		if temp_url not in visited  and link.get("href") != '/':
			#print(temp_url)
			if link.get("href")[-1] != '/':
				file.write(url+link.get("href")+"\n")
				print(link.get("href")+" <----- Scraped")

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
