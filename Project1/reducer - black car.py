#!/usr/bin/python


car_count = 0
cluster_count = 0

for line in sys.stdin:
    line = line.strip()
    group, counts = line.split('\t')
    streets = [int(x.strip(" '")) for x in streets]
    try: 
      car_count = car_count + 1
      if streets[1] == 1:
        cluster_count = cluster_count + 1

print('The likelihood of a black car getting a ticket at 34510, 10030, 34050 is ' + str(cluster_count / car_count) + '.')
    
 
