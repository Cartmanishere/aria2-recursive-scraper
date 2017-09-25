# Aria2 Recursive Download
A simple scraper and bash script combination to download open directories recursively using aria2 instead of wget.

I use python BeautifulSoup to scrape an open directory and make a directory structure with relevant link to files stored in links.txt
Then the simple bash script just goes into every directory and downloads the files in the links.txt using aria2c

The scraper will need some tweaking based on what directory you are trying to download.
So consider this as just a bare body scraper that needs to be customized according the situation and requirement.
