cwd=$PWD
find . -type d -print0 |
  while IFS= read -rd '' dir;
do
	cd "$dir"
	echo "Downloading from ${dir}"
	aria2c -c --auto-file-renaming=false -i links.txt
	cd "$cwd"
done