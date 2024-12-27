
class Dude:
    """
    Has attributes:
        name: str = Name of the Dude instance
        location: tuple[float, float] = (x, y) position

    Has methods:
        is_near(self, dudes: list[Dude], length: float) -> list[str]:
            Returns a list of all the Dudes which are within a distance of length. 
            E.g. 
            If there are Dudes in locations (0, 1), (2, 0), (0, 3)
            The length is 2.5
            and self is at (0, 0)
            Then the names of the dudes at (0, 1), (2, 0) are returned. 

        Can be casted to a string (both str and repr), both return the name of the Dude
    """
    def __init__(self, name: str, location: tuple[int]):
        pass

    def is_near(self, dudes: list, length: float) -> list[str]:
        pass
