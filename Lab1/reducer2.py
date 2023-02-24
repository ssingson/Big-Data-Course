#!/usr/bin/python 

from operator import itemgetter
from collections import defaultdict
import sys

top = defaultdict(list)


for line in sys.stdin:
	line = line.strip().split('\t')
	hr_ip, count = line
	
	#Pulls the hour data from the key 
	hr, ip = hr_ip.split(']')
	hr = hr[1:3]

	try:
		#Based on the hour creates a list of IP address and the number of entries it has 
		hr = int(hr)
		count = int(count)    
		top[hr].append([ip, count])

	except ValueError:
		pass 

#For each hour (including if filtered), pulls the top 3 IP addresses based on number of entries and prints the results. 
for i in range(24):
    top_n = sorted(top[i], key=lambda v:v[1], reverse=True)[0:3]
    print('%s\t%s' % (i, top_n))
