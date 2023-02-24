#!/usr/bin/python

# Pushes the data from reduce 1 to reducer 2 without data loss. 
import sys

for line in sys.stdin:
  sys.stdout.write(line) 
