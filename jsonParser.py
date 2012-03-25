#!/usr/bin/env python

import json

fp = open('config.json', 'r')
d = json.load(fp)
print 'There are '
print len(d['sites'])
print ' sites.'

print(d['sites'][0]['name'])
