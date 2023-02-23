#!/usr/bin/python
# --*-- coding:utf-8 --*--
import re
import sys

print(sys.argv[1])
print(sys.argv[2])
pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*? ')
for line in sys.stdin:
    match = pat.search(line)
    if match:
        if ((int(match.group('hour')) >= 3) and (int(match.group('hour')) <= 8)):
            print('%s\t%s' % ('[' + match.group('hour') + ':00' + ']' + match.group('ip'), 1))
