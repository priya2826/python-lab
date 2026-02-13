import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

p1 = Point(1, 2)
p2 = Point(4, 6)

print(f"{p2.distance_from_origin():.2f}")
print(f"Distance from P1 to P2: {p1.distance(p2):.2f}")
