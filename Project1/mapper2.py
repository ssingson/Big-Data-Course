#!/usr/bin/python

import re
import sys
import random 
import pandas as pd

centroids = []

for line in sys.stdin[0]: 
    line = [float(x) for x in line.strip('(').strip('\n').strip(')').split(',')]
    centroids.append(line)

lines = [s.split(',') for s in sys.stdin[1]]
columns = lines[0]
columns.append('Extra Line')

df = pd.DataFrame(data = lines[1:], columns = columns)

for index, row in df.iterrows():
    min_distance = float('inf')
    centroid = 0
    for i in range(len(centroids)): 
      distance = abs(int(row['Street Code1']) - int(centroids[i][0])) + abs(int(row['Street Code2']) - int(centroids[i][1])) + abs(int(row['Street Code3']) - int(centroids[i][2]))
      if distance < min_distance: 
        min_distance = distance
        centroid = i
    print('%s\t%s' % ( centroids[centroid], (row['Street Code1'], row['Street Code2'],row['Street Code3'])))
