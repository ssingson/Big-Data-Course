#!/usr/bin/python

import re
import sys
import random 
import pandas as pd

centroids = []

for line in sys.stdin[1]: 
    line = [float(x) for x in line.strip('(').strip('\n').strip(')').split(',')]
    centroids.append(line)
    
n = 0
for line in sys.stdin[0]: 
   if n == 0:
      n += 1
   else:
      try: 
        min_distance = float('inf')
        centroid = 0
        line = line.strip().split(",")
        for i in range(len(centroids)): 
          distance = abs(int(line[10] - int(centroids[i][0])) + abs(int(line[11] - int(centroids[i][1])) + abs(int(line[12] - int(centroids[i][2]))
          if distance < min_distance: 
            min_distance = distance
            centroid = i
         print('%s\t%s' % (centroids[i], '(' + line[10] + ',' + line[11] + ',' + line[12] + ')'))
      except ValueError: 
         pass
