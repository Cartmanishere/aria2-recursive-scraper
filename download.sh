
for d in */;
do
	cd "$d"
	echo "Downloading from ${d}"
	aria2c -i links.txt
	cd ../
done