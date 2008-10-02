#!/usr/bin/env python
from mcache import *
from s2t import *
from s2t_phrase import *

s2t_db = mcache('s2t.db')
t2s_db = mcache('t2s.db')
s2tp_db = mcache('s2t_p.db')
t2sp_db = mcache('t2s_p.db')

for k,v in s_2_t.iteritems():
    s2t_db.addu(k,v)
for k,v in t_2_s.iteritems():
    t2s_db.addu(k,v)
for k,v in s_2_t_phrase.iteritems():
    s2tp_db.addu(k,v)
for k,v in t_2_s_phrase.iteritems():
    t2sp_db.addu(k,v)
