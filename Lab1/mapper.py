#!/usr/bin/python
# --*-- coding:utf-8 --*--

import re
import sys

# Maps the data pulling the hour and IP address and having a count of 1 for later reducing.  
pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*? ')
for line in sys.stdin:
    match = pat.search(line)
    if match:
        print('%s\t%s' % ('[' + match.group('hour') + ':00' + ']' + match.group('ip'), 1))
