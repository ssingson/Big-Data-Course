#!/usr/bin/python

clusters = set()
dict_0.5_count = {}
dict_ticket_count = {}

for line in sys.stdin:
    line = line.strip()
    group, counts = line.split('\t')
    clusters.append(group) 
    streets = [int(x.strip(" '")) for x in streets]
    try: 
      dict_ticket_count[group] = dict_ticket_count.get(group, 0) + 1
      if streets[1] == 1:
        dict_0.5_count[group] = dict_0.5_count.get(group, 0) + 1
      else: 
        dict_0.5_count[group] = dict_0.5_count.get(group, 0)

for cluster in clusters: 
  if dict_0.5_count[cluster] > 0: 
    print('%s\t%s' % (dict_ticket_count[group], str(dict_ticket_count[cluster])))
