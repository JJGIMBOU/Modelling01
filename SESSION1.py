# you define classes with class
class Point:  # to show a point on the y and x axis
    def __init__(self, x, y):
        """internalize the point
        param x: the x coordinate
        param y: the y coordinate
        """
        self.x = x
        self.y = y
    def __str__(self):
        """
        Return the string representation of the point
       :return: p<x, y>
        """
        return f"p<{self.x}, {self.y}>"
    def __repr__(self):
        return self.__str__()
    def distance_origin(self):
        """
        Return the distance from the origin to the point
        :return: float
        """
        return (self.x**2 + self.y**2)**0.5
    def distance_other(self, other):
        """
        Return the distance from the other point to the point
        :param other: another point
        :return: the distance from the other point to the point
        """
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
    def __lt__(self, other):
        """
        compare two points objects
        :param other: the other point object
        :return: bool True or False
        """
        return self.distance_origin() < other.distance_origin()


if __name__ == '__main__':
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    p3 = Point(5, 6)
    # instantiate the point class
    p1 = Point(1, 2)
    p2 = Point(x=3, y=4)
    print(p1.x, p1.y) # result shows location in the internal memory
    p3 = Point(4,3)
    print(p3.distance_origin())
    p4 = Point(12, 5)
    print(p4.distance_origin())
    points = [p1, p2, p3, p4, Point(-2, 6)]
    points.append(Point(-5, -5))
    print(points[4].x) #to print the 5th point
    print(points[5].distance_origin()) #same thing
    print(points)
    points.sort()
    print(points)
    print(Point(7, 11).distance_other(Point(7,15))) # expect 4
