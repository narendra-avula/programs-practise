__author__ = 'Naidu'

# m = 8
# a = lambda x,y :(x *m)/y
# print a(2,3)

# map = 7
# def func():
#     return map
# print func()

# class A(object):
#     def __repr__(self):
#         return 'ista A'
#
# a = A()
# b = a
# del a
# print b

# class Human(object):
#     def __setattr__(self, name, value):
#         if name == 'gender':
#             self.gender = value
#         else:
#             raise AttributeError("gendder")
#
#
# h = Human()
# h.name = 'Mary'
# h.gender = "female"
# print h.gender

# def func():
#     return 1,2,3
# (a,b) = func()

# l = [i for i in xrange(123)]
# x = (i for i in xrange(123))
# print l
# print x

# class A:
#     pass
#
# class B:
#     pass
#
# a = A()
# b = B()
# print type(a) == type(b)

class A(object):
    def calc(self):
        return 17

class B(object):
    def calc(self):
        return 6

class C(A, B):
    pass

c = C()
print c.calc()