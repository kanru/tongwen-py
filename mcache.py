#!/usr/bin/env python
import anydbm

class mcache(object):
    def __init__(self, f):
        self.db = anydbm.open(f, 'c')
    def __del__(self):
        self.db.close()
    def add(self, k, v):
        self.db[k] = v
    def addu(self, k, v):
        self.add(k.encode('utf8'), v.encode('utf8'))
    def delete(self, k):
        if self.db.has_key(k):
            del self.db[k]
    def deleteu(self, k):
        self.delete(k.encode('utf8'))
    def has_keyu(self, k):
        return self.db.has_key(k.decode('utf8'))
    def keyu(self, k):
        return self.db[k.decode('utf8')]

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        exit(1)
    elif sys.argv[1] == '-a':
        m = mcache(sys.argv[2])
        m.add(sys.argv[3], sys.argv[4])
    elif sys.argv[1] == '-d':
        m = mcache(sys.argv[2])
        m.delete(sys.argv[3])
