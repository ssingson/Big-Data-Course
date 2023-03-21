#!/usr/bin/python
# --*-- coding:utf-8 --*--

import re
import sys

for line in sys.stdin: 
   try: 
      line = line.strip().split(",")
      print('%s\t%s' % (random.randint(1,3), '(' + line[10] + ',' + line[11] + ',' + line[12] + ')'))
