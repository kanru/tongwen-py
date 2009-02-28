#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mcache import *
import sys

def dbpath():
    import os.path, sys
    if __name__ == '__main__':
        filename = sys.argv[0]
    else:
        filename = __file__
    return os.path.abspath(os.path.dirname(filename))

s2t = mcache(dbpath()+'/s2t.db')
t2s = mcache(dbpath()+'/t2s.db')
s2tp = mcache(dbpath()+'/s2t_p.db')
t2sp = mcache(dbpath()+'/t2s_p.db')

f = file(sys.argv[1])
lines = f.readlines()
all = ''.join(lines).decode('UTF-8')
copy = []

for c in all:
    if s2t.db.has_key(c.encode('UTF-8')):
        copy.append(s2t.db[c.encode('UTF-8')])
    else:
        copy.append(c.encode('UTF-8'))

out = ''.join(copy)
for k, v in s2tp.db.iteritems():
    if v != '':
        out = out.replace(k, v)
print out
