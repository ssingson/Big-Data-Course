#!/usr/bin/python

import re
import sys
import os 
import random 
import pandas as pd

centroids = []
centroids_count = []

for line in sys.stdin:
    input_file = os.environ['map_input_file']
     if input_file.startswith('/output/'):
        line = [float(x) for x in line.strip('(').strip('\n').strip(')').split(',')]
        centroids.append(line)
    

#Only counts black cars
n = 0
for line in sys.stdin:
  if line[34] == 'BLK': 
    input_file = os.environ['map_input_file']
         if input_file.startswith('/input/'):
           # removes the column headers row
            if n == 0:
              n += 1
           else:
              try: 
                min_distance = float('inf')
                centroid = 0
                line = line.strip().split(",")
                for i in range(len(centroids)): 
                  distance = ((int(line[10] - int(centroids[i][0]))) ** 2 + ((int(line[11] - int(centroids[i][1]))) ** 2 + ((int(line[12] - int(centroids[i][2]))) ** 2) ** 0.5
                  if distance < min_distance: 
                    min_distance = distance
                    centroid = i
                 centroids_count[centroid] = centroids_count[centroid] + 1                                                           
              except ValueError: 
                 pass

#find centroid of the location specified
for i in range(len(centroids)): 
  min_distance = float('inf')
  centroid = 0                                                                          
  distance = ((34510 - int(centroids[i][0]))) ** 2 + ((10030 - int(centroids[i][1]))) ** 2 + ((34050 - int(centroids[i][2]))) ** 2) ** 0.5
  if distance < min_distance: 
    min_distance = distance
    centroid = i

#pushes all under 'Black Car' so in one group, each push the cluster's number of black cars and if this cluster is where the desired location is in                              
for i in len(centroids): 
  if i == centroid:
    print('%s\t%s' % ('Black Car', '(' + str(centroids_count[i]) + ',' + str(1) + ')'))
  else:                      
    print('%s\t%s' % ('Black Car', '(' + str(centroids_count[i]) + ',' + str(0) + ')'))

                                                                            
