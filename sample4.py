import math

class Point:
    def __init__(self, a, b, c):
        self.x = a
        self.y = b
        self.z = c

    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def distance(self, point2):
        return math.sqrt(
            (self.x - point2.x) ** 2 +
            (self.y - point2.y) ** 2 +
            (self.z - point2.z) ** 2
        )


# Input for first point
x1, y1, z1 = map(int, input("Enter P1 (x y z): ").split())

# Input for second point
x2, y2, z2 = map(int, input("Enter P2 (x y z): ").split())

# Create objects
p1 = Point(x1, y1, z1)
p2 = Point(x2, y2, z2)

# Output results (formatted to 2 decimal places)
print(f"Distance from origin to P1: {p1.distance_from_origin():.2f}")
print(f"Distance from origin to P2: {{p2.distance_from_origin():.2f}")
print(f"Distance from P1 to P2: {p1.distance(p2):.2f}")
