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
        for i in range(len(centroids)): 
          distance = abs(int(row['Street Code1']) - int(centroids[i][0])) + abs(int(row['Street Code2']) - int(centroids[i][1])) + abs(int(row['Street Code3']) - int(centroids[i][2]))
          if distance < min_distance: 
            min_distance = distance
            centroid = i
            line = line.strip().split(",")
         print('%s\t%s' % (random.randint(1,3), '(' + line[10] + ',' + line[11] + ',' + line[12] + ')'))
      except ValueError: 
         pass
