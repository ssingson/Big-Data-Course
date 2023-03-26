from operator import itemgetter
import sys

  dict_ticket_count = {}
  dict_streetcode1_sum = {}
  dict_streetcode2_sum = {}
  dict_streetcode3_sum = {}

 for line in sys.stdin: 
      line = line.strip()
      group, streets = line.split('\t')
      streets = [int(x.strip(" '")) for x in streets.strip('()').split(',')]
      try:
          dict_ticket_count[group] = dict_ticket_count.get(group, 0) + 1
          dict_streetcode1_sum[group] = dict_streetcode1_sum.get(group, 0) + streets[0]
          dict_streetcode2_sum[group] = dict_streetcode1_sum.get(group, 0) + streets[1]
          dict_streetcode3_sum[group] = dict_streetcode1_sum.get(group, 0) + streets[2]


      except ValueError:
          pass


sorted_ticket_count = sorted(dict_ticket_count.items(), key=itemgetter(0))
sorted_streetcode1_sum = sorted(dict_streetcode1_sum.items(), key=itemgetter(0)) / sorted(dict_ticket_count.items(), key=itemgetter(0))
sorted_streetcode2_sum = sorted(dict_streetcode2_sum.items(), key=itemgetter(0)) / sorted(dict_ticket_count.items(), key=itemgetter(0))
sorted_streetcode3_sum = sorted(dict_streetcode3_sum.items(), key=itemgetter(0)) / sorted(dict_ticket_count.items(), key=itemgetter(0))


cluster_distance = [] 

 for line in sys.stdin: 
      line = line.strip()
      group, streets = line.split('\t')
      streets = [int(x.strip(" '")) for x in streets.strip('()').split(',')]
      try:
          distance_streetcode1[group] = (((sorted_streetcode1_sum.get(group, 0) - streets[0]) ** 2) + ((sorted_streetcode2_sum.get(group, 0) - streets[1]) ** 2) + ((sorted_streetcode3_sum.get(group, 0) - streets[2]) ** 2)) ** 0.5 

      except ValueError:
          pass

for i in range(len(sorted_ticket_count)):
  print(str((sorted_streetcode1_sum[i][1] / sorted_ticket_count[i][1], sorted_streetcode2_sum[i][1] / sorted_ticket_count[i][1], sorted_streetcode3_sum[i][1] / sorted_ticket_count[i][1])), )
