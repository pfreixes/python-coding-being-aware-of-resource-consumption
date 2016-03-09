#!/usr/bin/env python
import timeit

print "Get the differnece between list, dict and set containers with 10K of elements"

def dict_diff(a, b):
    only_a = set((key for key in a.keys() if key not in b))
    only_b = set((key for key in b.keys() if key not in a))
    assert len(only_a | only_b) == 20

def list_diff(a, b):
    only_a = set((item for item in a if item not in b))
    only_b = set((item for item in b if item not in a))
    assert len(only_a | only_b) == 20

print "Using list type: {}".format(
        timeit.timeit("list_diff((xrange(0, 10**4)), (xrange(10, 10**4+10)))", number=1, setup="from __main__ import list_diff")
)

print "Using dict type: {}".format(
        timeit.timeit("dict_diff({i:i for i in xrange(0, 10**4)}, {i:i for i in xrange(10, 10**4+10)})", number=1, setup="from __main__ import dict_diff")
)

print "Using dict type + viewkeys: {}".format(
        timeit.timeit("{i:i for i in xrange(0, 10**4)}.viewkeys() ^ {i:i for i in xrange(10, 10**4+10)}.viewkeys()", number=1)
)

print "Using set type: {}".format(
    timeit.timeit("assert len(set((i for i in xrange(0, 10**4))) ^ set((i for i in xrange(10, 10**4+10)))) == 20", number=1)
)

print "Get the differnece between dit, set containers with 10M of elements"

print "Using dict type: {}".format(
        timeit.timeit("dict_diff({i:i for i in xrange(0, 10**7)}, {i:i for i in xrange(10, 10**7+10)})", number=1, setup="from __main__ import dict_diff")
)

print "Using set type: {}".format(
    timeit.timeit("assert len(set((i for i in xrange(0, 10**7))) ^ set((i for i in xrange(10, 10**7+10)))) == 20", number=1)
)
