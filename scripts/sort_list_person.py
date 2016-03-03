import operator

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return self.name

l = [Person('foo', 24), Person('bar', 12), Person('aaaaa', 89)]
print sorted(l, key=operator.attrgetter('name'))
