#Map 1
import re
import sys
import random 
import pandas as pd

lines = [s.split(',') for s in lines]
columns = lines[0].copy()
columns.append('Extra Line')

df = pd.DataFrame(data = lines, columns = columns)

with open('data.log', 'w') as g:
  for index, row in df[1:20].iterrows():
      print()
      g.write('%s\t%s' % ( random.randint(1,3), (row['Street Code1'], row['Street Code2'],row['Street Code3'])))
      g.write('\n')
