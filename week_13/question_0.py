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
    
    def distance(self, point: tuple[float]) -> float:
        pass

    def __str__(self):
        pass

    # You may add more methods here

def within_open_circle(point: tuple[float], circles: set[Circle]) -> Circle:
    """
    Determines whether point is any of the circles in the set
    If not, then add to the set and return a Circle with center (0, 0)
    and radius such that the point is on edge of the circle. 
    If the point is within one of the circles,
    then return the Circle that's center is closest to the point.

    I would recommend drawing on paper, what this situation looks like. 
    """

# You may add more functions here. 
    
def main():
    circle_1: Circle = Circle((1, 1), 10)
    circle_2: Circle = Circle((4, 1), 2)
    circle_3: Circle = Circle((-5, 1), 13)
    circle_4: Circle = Circle((1, 11), 1000)
    circles: set[Circle] = {circle_1, circle_2, circle_3, circle_4}
    output_circle: Circle = within_open_circle((3, 3), circles)
    print(output_circle)

if __name__ == "__main__":
    main()
