from SESSION1 import Point

class ColorPoint(Point):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    def __str__(self):
        return f"{self.color}:cp< {self.x}, {self.y}"

p1 = ColorPoint(1,2, "green")
p2 = ColorPoint(10,10, "red")
print(p1.x, p1.y, p1.color)
print(p2)
print(p2.distance_origin())
points = [p1, p2]
points.append(Point(2, 0))
points.append(-1)
points.sort()
print(points)