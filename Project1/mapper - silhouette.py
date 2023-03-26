#!/usr/bin/python

import re
import sys
import os 
import random 
import pandas as pd

centroids = {}

for line in sys.stdin:
    input_file = os.environ['map_input_file']
     line = line.strip()
     group, streets = line.split('\t')
     if input_file.startswith('/output/'):
        centroids[group] = streets
    
    
n = 0
for line in sys.stdin:
    input_file = os.environ['map_input_file']
     if input_file.startswith('/input/'):
       if n == 0:
          n += 1
       else:
          try: 
            #find closest cluster
            min_distance = float('inf')
            centroid = 0
            line = line.strip().split(",")
            for centroid in centroids.keys: 
              distance = ((int(line[10] - int(centroid[0]))) ** 2 + (abs(int(line[11] - int(centroid[1]))) ** 2 + (abs(int(line[12] - int(centroid[2]))) ** 2) ** 0.5
              if distance < min_distance: 
                min_distance = distance
                centroid = i
            
            #find total distance of centroids to point                                                             
            distance = 0
            line = line.strip().split(",")
            for centroid in centroids.keys: 
              distance = distance + ((int(line[10] - int(centroid[0]))) ** 2 + (abs(int(line[11] - int(centroid[1]))) ** 2 + (abs(int(line[12] - int(centroid[2]))) ** 2) ** 0.5
             
           print('%s\t%s' % ('All Points', '(' + str(distance / len(centroids)) + ',' +  str(centroids[i]) ')'))
          except ValueError: 
             pass
