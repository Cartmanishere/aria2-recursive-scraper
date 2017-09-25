from multiprocessing import Pool
from dirmaker import *

if __name__ == '__main__':
	init_urls = tuple(open("lynda.txt", "r"))
	p = Pool(5)
	metalist = p.map()