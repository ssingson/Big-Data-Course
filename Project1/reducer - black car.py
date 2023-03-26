#!/usr/bin/python


car_count = 0

for line in sys.stdin:
    line = line.strip()
    group, counts = line.split('\t')
    streets = [int(x.strip(" '")) for x in streets.strip('(').strip(')').split(',')]
    try: 
      car_count = car_count + streets[0]
      if streets[1] == 1:
        cluster_count = streets[0]

print('The likelihood of a black car getting a ticket at 34510, 10030, 34050 is ' + str(cluster_count / car_count) + '.')
    
 
