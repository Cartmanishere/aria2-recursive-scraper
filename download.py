import os

def download():
	os.system("aria2c --file-allocation=none -c --auto-file-renaming=false -i links.txt")

folders = [ x[0] for x in os.walk(os.getcwd()) ]
folders.sort()
download()

for i in folders:
	os.chdir(i.encode("utf-8").decode())
	download()
