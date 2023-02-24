#!/usr/bin/python
from operator import itemgetter
import sys

dict_ip_count = {}

for line in sys.stdin:
    line = line.strip()
    #splits the key and value based on the tab 
    ip, num = line.split('\t')
    try:
        num = int(num)
        #Pulls the hour and the address under IP then every time a new entry has the same information adds 1 to the count.  
        dict_ip_count[ip] = dict_ip_count.get(ip, 0) + num

    except ValueError:
        pass

#Sorts the data from smallest to largest. 
sorted_dict_ip_count = sorted(dict_ip_count.items(), key=itemgetter(0))
for ip, count in sorted_dict_ip_count:
#Sends the full list of the ip and the count to the second mapreduce function. 
    print('%s\t%s' % (ip, count))
