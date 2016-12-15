__author__ = 'narendra'


# class Point:
#
#     def __init__(self):
#         self.x = 0
#         self.y = 0
#
# p = Point()
# q = Point()
# print(p.x, p.y, q.x, q.y)
# p.x = 3
# p.y = 4
# print(p.x, p.y, q.x, q.y)
# print("(x={0}, y={1})".format(p.x, p.y))
# distance_squared_from_origin = p.x * p.x + p.y * p.y
# print distance_squared_from_origin

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
# p = Point(3,4)
# q = Point(5,6)
# r = Point()   # Origin
# print r.x , r.y


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def midpoint(self, point1, point2):
        mx = ( point1.x + point2.x ) / 2
        my = ( point1.y + point2.y ) / 2
        return Point(mx, my)

    def distance_between_two_points(self, other):
        'Compute the Euclidean distance between two Point objects'
        delta_x = self.x - other.x
        delta_y = self.x - other.y
        return ( ( delta_x ** 2 ) + ( delta_y ** 2 ) ) ** 0.5

    def reflect_x(self):
        return Point(-self.x, self.y)

    def slope_from_origin(self):
        return float( self.y ) /self.x


p = Point(3, 4)
q = Point(5, 12)
print p
print q
# print Point().midpoint(p, q)
# print p.distance_from_origin()
# print p.distance_between_two_points(q)
# print p.reflect_x()
print Point(4,10).slope_from_origin()