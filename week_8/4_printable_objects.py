
class Orange:
    def __init__(self):
        self.colour: str = "Orange"

class Person:
    def __init__(self, f_name: str, l_name: str, no_kills: float):
        self.f_name: str = f_name
        self.l_name: str = l_name
        self.no_kills: float = no_kills
    
    # This is run whenever your object is casted to a string
    # E.g. str(object) 
    def __str__(self) -> str:
        return f"My name is {self.f_name} {self.l_name}, and I have killed {self.no_kills} people!"
    
    # This is run whenever the object is casted to a repr
    # E.g. repr(object)
    def __repr__(self) -> str:
        return f"Name: {self.f_name} {self.l_name}, Number of Kills: {self.no_kills}"
        # return str(self)

def main():
    # orange()
    person()

def orange():
    my_orange: Orange = Orange()
    # This is the default behaviour when you print an instance of a class.
    print(f"{my_orange}")
    print(f"{my_orange = }")
    print(f"{my_orange!r}")

def person():
    nicholas: Person = Person("Nicholas", "Bertollo", 6.9)
    # What is a repr?
    # A repr is a string representation of an object which is useful for debugging
    # In a lot of cases, str(object) == repr(object), however this isn't the case here 
    print(f"{nicholas}") # str
    print(f"{nicholas = }") # Repr
    print(f"{nicholas!r}") # repr

if __name__ == "__main__":
    main()