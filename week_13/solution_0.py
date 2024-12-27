import math

class Circle:
    """
    This class represents the idea of a circle in 2D space. 
    """
    def __init__(self, center: tuple[float], radius: float):
        """
        This has a center attribute and a radius attribute.
        If the radius is negative, then raise a ValueError with the message:
            "Cannot have negative radius"
        """
        self.center: tuple[float] = center
        if radius < 0:
            raise ValueError("Cannot have negative radius")
        self.radius: float = radius
    
    def distance(self, point: tuple[float]) -> float:
        """
        This finds the distance between the center
        of the circle and the point. 
        """
        # This is just the length of the line between the two points. 
        # However this is just pythagorus!
        return math.sqrt((point[0] - self.center[0]) ** 2 + (point[1] - self.center[1]) ** 2)
    
    def __str__(self) -> str:
        return f"Centre: {self.center}, Radius: {self.radius}"

def within_open_circle(point: tuple[float], circles: set[Circle]) -> Circle:
    """
    Determines whether point is in any of the circles in the set
    If not, then add to the set and return a Circle with center (0, 0)
    and radius such that the point is on edge of the circle. 
    If the point is within one of the circles,
    then return the Circle that's center is closest to the point.

    I would recommend drawing on paper what this situation looks like. 
    """
    # First let's iterate over the circles and check whether 
    # the point is within any of the circles. 
    # If we find a a circle that our point is in, 
    # we only update this information if it's closer than
    # previously
    current_closest: Circle = Circle((float("inf"), float("inf")), float("inf"))
    for circle in circles:
        if circle.distance(point) <= circle.radius and circle.distance(point) <= current_closest.distance(point):
            # This means that the point is within the circle
            # and that it's closer than before
            current_closest: Circle = circle
    
    if current_closest.radius == float("inf"):
        distance: float = math.sqrt(point[0] ** 2 + point[1] ** 2)
        new_circle: Circle = Circle((0, 0), distance)
        circles.add(new_circle)
        return new_circle
    else:
        return current_closest
    
    
def main():
    circle_1: Circle = Circle((1, 1), 10)
    circle_2: Circle = Circle((4, 1), 2)
    circle_3: Circle = Circle((-5, 1), 13)
    circle_4: Circle = Circle((1, 11), 1000)
    circles: set[Circle] = {circle_1, circle_2, circle_3, circle_4}
    print(within_open_circle((3, 3), circles))
    print(within_open_circle((0, 0), circles))
    print(within_open_circle((10, 10), circles))
    print(within_open_circle((1000000000, 10000), circles))

if __name__ == "__main__":
    main()