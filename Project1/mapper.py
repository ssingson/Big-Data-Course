#!/usr/bin/python
import re
import sys
import random 
import pandas as pd

lines = [s.split(',') for s in sys.stdin]
columns = lines[0]
columns.append('Extra Line')

df = pd.DataFrame(data = lines[1:], columns = columns)

for index, row in df.iterrows():
   print('%s\t%s' % ( random.randint(1,3), (row['Street Code1'], row['Street Code2'],row['Street Code3'])))
