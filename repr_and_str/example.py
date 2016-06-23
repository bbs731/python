# __str__ cater for print and console output
# __repr__ means eval(repr(obj)) = obj
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)
    def __str__(self):
        return '({0.x}, {0.y})'.format(self)

c = Pair(2, 3)
print (repr(c))
print (eval(repr(c)))
