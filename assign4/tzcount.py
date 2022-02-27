#!/usr/bin/python

import sys
import re

def sortTimezone(timezone): 
  if timezone[0] == '-':
    return -int(timezone[2])
  else:
    return int(timezone[2])

file = sys.stdin.read()
timezones = re.findall(r'[+-]0[0-9]00', file)
count = {}

for timezone in timezones:
  if timezone in count:
    count[timezone] += 1
  else:
    count[timezone] = 1
    
for key in sorted(count, key=sortTimezone):
  print('%s %s' % (key, count[key]))