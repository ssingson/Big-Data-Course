#Map 1
import re
import sys
import random 
import pandas as pd

df = pd.read_csv(sys.stdin)

for index, row in df.iterrows():
  print('%s\t%s' % ( random.randint(1,3), (row['Street Code1'], row['Street Code2'],row['Street Code3'])))
