import os

folders = [ x[0] for x in os.walk(os.getcwd()) ]

for i in folders:
	os.chdir(i.encode("utf-8").decode())
	os.system("aria2c --file-allocation=none -c --auto-file-renaming=false -i links.txt")
