#!/usr/bin/env python
import random

from pympler import asizeof

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class PersonSlots(object):
    __slots__ = ('name', 'age')
    def __init__(self, name, age):
        self.name = name
        self.age = age


l = [Person('a', i) for i in xrange(0, 10**5)]
print "Memory used by 100K Person elements : {} MB".format(asizeof.asizeof(l)/1024**2)
l2 = [PersonSlots('a', i) for i in xrange(0, 10**5)]
print "Memory used by 100K Person elements using slots: {} MB".format(asizeof.asizeof(l2)/1024**2)
