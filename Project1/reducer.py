#first reduce

from operator import itemgetter
import sys

dict_ticket_count = {}
dict_streetcode1_sum = {}
dict_streetcode2_sum = {}
dict_streetcode3_sum = {}

with open('data.log', 'w') as g: #this line change for submission
  
  for line in lines:
    line = line.strip()
    group, streets = line.split('\t')
    group = int(group)
    streets = [int(x.strip(" '")) for x in streets.strip('()').split(',')]
    try:
        group = int(group)
        dict_ticket_count[group] = dict_ticket_count.get(group, 0) + 1
        dict_streetcode1_sum[group] = dict_streetcode1_sum.get(group, 0) + streets[0]
        dict_streetcode2_sum[group] = dict_streetcode1_sum.get(group, 0) + streets[1]
        dict_streetcode3_sum[group] = dict_streetcode1_sum.get(group, 0) + streets[2]


    except ValueError:
        pass


sorted_ticket_count = sorted(dict_ticket_count.items(), key=itemgetter(0))
sorted_streetcode1_sum = sorted(dict_streetcode1_sum.items(), key=itemgetter(0))
sorted_streetcode2_sum = sorted(dict_streetcode2_sum.items(), key=itemgetter(0))
sorted_streetcode3_sum = sorted(dict_streetcode3_sum.items(), key=itemgetter(0))

with open('data.log', 'w') as g:
  for i in range(len(sorted_ticket_count)):
    g.write(str((sorted_streetcode1_sum[i][1] / sorted_ticket_count[i][1], sorted_streetcode2_sum[i][1] / sorted_ticket_count[i][1], sorted_streetcode3_sum[i][1] / sorted_ticket_count[i][1])))
    g.write('\n')
