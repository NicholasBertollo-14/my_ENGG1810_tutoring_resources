
class Cat:
    """
    Representation of a cat. 
    Can meow and be killed.
    """
    def __init__(self, name: str, no_lives: int = 1):
        """
        This is the constructor, if the number of lives
        input into the constructor is less than 0, 
        then set it to 0, 
        if the input into the constructor is greater than 9, 
        then set it to 9
        """
        self.name: str = name
        if no_lives < 0:
            self.no_lives: int = 0
        elif no_lives > 9:
            self.no_lives: int = 9
        else:
            self.no_lives: int = no_lives
    
    def meow(self):
        """
        This will cause the cat to meow. 
        In this case this means printing
        meeeeeow
        with the number of 'e''s representing the 
        cat's number of lives. 
        If the cat has 0 lives, then it cannot meow.
        """
        if self.no_lives > 0:
            print(f"m{'e' * self.no_lives}ow")
        
    def kill(self):
        """
        This causes the cat to lose a life.
        If the cat has run out of lives, 
        then you should set the name of the cat to have R.I.P.
        in front of the cat's name, and not allow the cat to 
        lose amymore lives. 
        """
        if self.no_lives == 0:
            return
        self.no_lives -= 1
        if self.no_lives == 0:
            self.name: str = f"R.I.P. {self.name}"
