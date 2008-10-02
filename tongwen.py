#!/usr/bin/env python
# -*- coding: utf8 -*-

from mcache import *
import sys

s2t = mcache('s2t.db')
t2s = mcache('t2s.db')
s2tp = mcache('s2t_p.db')
t2sp = mcache('t2s_p.db')

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
