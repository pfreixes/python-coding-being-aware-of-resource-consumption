#!/usr/bin/env python
import sys

print "1. Differnece between list, dict and set containers with 1M of numbers regarding the size and container overhead"
l = sys.getsizeof({i:i for i in xrange(0, 10**6)})
d = sys.getsizeof(set([i for i in xrange(0, 10**6)])) 
s = sys.getsizeof([i for i in xrange(0, 10**6)])
print "Sizeof with dict type: {}M, overhead per item {}b".format(l/1024**2, l/10**6)
print "Sizeof with set type: {}M, overhead per item {}b".format(d/1024**2, d/10**6)
print "Sizeof with list type: {}M, overhead per item {}b".format(s/1024**2, s/10**6)
print "-"*10
print "2. Caution sizeof depends on the type implementation, for example have a look to the list https://github.com/python/cpython/blob/master/Objects/listobject.c#L2317"
print "the list container returns the size of its internal structure, leaving aside the size of the object stored"
print "Sizeof 1M list wit 32 bytes elements: {}".format(sys.getsizeof(["x"*32 for i in xrange(0, 10**6)]) / 10**6)
print "Sizeof 1M list wit 512 bytes elements: {}".format(sys.getsizeof(["x"*512 for i in xrange(0, 10**6)]) / 10**6)
