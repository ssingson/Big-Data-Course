#!/usr/bin/python
# --*-- coding:utf-8 --*--

import re
import sys
import random

n = 0
for line in sys.stdin: 
   if n == 0:
      n += 1
   else:
      try: 
         line = line.strip().split(",")
         print('%s\t%s' % (random.randint(1,sys.argv[1]), '(' + line[10] + ',' + line[11] + ',' + line[12] + ')'))
      except ValueError: 
         pass
