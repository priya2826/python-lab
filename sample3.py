import math

class Point:
    def __init__(self, a, b, c):
        self.x = a
        self.y = b
        self.z = c

    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def distance(self, point2):
        xdiff = self.x - point2.x
        ydiff = self.y - point2.y
        zdiff = self.z - point2.z
        return math.sqrt(xdiff**2 + ydiff**2 + zdiff**2)



x1, y1, z1 = input("Enter the coordinates of first point P1 (x y z): ").split()
x1, y1, z1 = int(x1), int(y1), int(z1)


x2, y2, z2 = input("Enter the coordinates of second point P2 (x y z): ").split()
x2, y2, z2 = int(x2), int(y2), int(z2)


p1 = Point(x1, y1, z1)
p2 = Point(x2, y2, z2)

print("Distance from origin to P1:", p1.distance_from_origin())
print("Distance from origin to P2:", p2.distance_from_origin())
print("Distance from P1 to P2:", p1.distance(p2))
