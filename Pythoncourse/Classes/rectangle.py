import copy

__author__ = 'narendra'

class Point:
    def __init__(self,x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def same_coordinates(p1, p2):
        return (p1.x == p2.x) and (p1.y == p2.y)


class Rectangle:
    def __init__(self, position, width, height):
        self.corner = position
        self.width = width
        self.height = height

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        self.corner.x += dx
        self.corner.y += dy

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * ( self.width + self.height)


r = Rectangle(Point(0,0), 10, 5)
print r
print r.area()
print r.perimeter()

# p1 = Point(3,4)
# p2 = Point(3,4)
#
# p3 = copy.deepcopy(p1)
# p4 = copy.copy(p1)
# print p1 is p3
# print p1 is p4

# def same_coordinates(p1, p2):
#     return (p1.x == p2.x) and (p1.y == p2.y)
# print same_coordinates(p1, p2)
#
# p = Point(4, 2)
# s = Point(4, 2)
# print("== on Points returns", p == s)
# # By default, == on Point objects does a shallow equality test
#
# a = [2,3]
# b = [2,3]
# print("== on lists returns",  a == b)

# p = Point(3,4)
# print p
# box = Rectangle(Point(0, 0), 100, 200)
# bomb = Rectangle(Point(100, 80), 5, 10)
# print box
# print bomb
# box1 = Rectangle(Point(0,0), 100, 100)
# print box1
# box1.move(10, 10)
# print box1
# box1.grow(100, 150)
# print box1

# point1 = Point(3, 4)
# point2 = Point(3, 4)
# print point1 is point2
# point3 = point1
# print point1 is point3