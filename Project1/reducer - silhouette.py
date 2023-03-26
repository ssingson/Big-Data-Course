#!/usr/bin/python


silhouette_total = 0
ticket_count = 0

for line in sys.stdin: 
      line = line.strip()
      group, streets = line.split('\t')
      streets = [int(x.strip(" '")) for x in streets.strip('()').split(',')]  
      try: 
        ticket_count += 1
        silhouette_total = streets[1] - streets[0] / max(streets[1], streets[0])
        
print('The silhouette score of ' + str(sys.argv[1]) + 'clusters is ' + str(silhouette_total / ticket_count) + '.')
