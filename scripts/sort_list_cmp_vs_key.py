import timeit

print timeit.timeit('[x for x in xrange(10**6, 1, -1)].sort(cmp=lambda a,b: cmp(id(a),id(b)))', number=1)
print timeit.timeit('[x for x in xrange(10**6, 1, -1)].sort(key=id)', number=1)
print [x for x in xrange(10**6, 1, -1)].sort(key=id) == [x for x in xrange(10**6, 1, -1)].sort(cmp=lambda a,b: cmp(id(a),id(b)))
