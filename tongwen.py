#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mcache import *
import sys

def usage():
    print 'Usage: tongwen.py [-s2t] inputfile'
    exit(0)

def dbpath():
    import os.path, sys
    if __name__ == '__main__':
        filename = sys.argv[0]
    else:
        filename = __file__
    return os.path.abspath(os.path.dirname(filename))

if len(sys.argv) < 2:
    usage()

s2t = mcache(dbpath()+'/s2t.db')
t2s = mcache(dbpath()+'/t2s.db')
s2tp = mcache(dbpath()+'/s2t_p.db')
t2sp = mcache(dbpath()+'/t2s_p.db')

tb1 = s2t
tb2 = s2tp

inputf = sys.argv[1]
if inputf == '-t2s':
    if len(sys.argv) < 3:
        usage()
    else:
        tb1 = t2s
        tb2 = t2sp
        inputf = sys.argv[2]

f = file(inputf)
lines = f.readlines()
all = ''.join(lines).decode('UTF-8')
copy = []

for c in all:
    if tb1.db.has_key(c.encode('UTF-8')):
        copy.append(s2t.db[c.encode('UTF-8')])
    else:
        copy.append(c.encode('UTF-8'))

out = ''.join(copy)
for k, v in tb2.db.iteritems():
    if v != '':
        out = out.replace(k, v)
print out
