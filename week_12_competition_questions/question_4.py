
class Person:
    def __init__(self, name: str, friendliness: int):
        """
        A person has the attributes name and friendliness
        """
    
    def interaction(self, mood: str):
        """
        Will change friendliness by mood.
        If their mood is "happy" then increase friendliness by 10
        If their mood is "bored" then decrease friendliness by 3
        If their mood is "sad" then decrease friendliness by 10
        """
    
def invite_to_party(me: Person, friends: list[Person]) -> dict[str, int]:
    """
    This function performs an interaction with every person
        If their name starts with an 'a' then they are happy
        If their name starts with a 'c' then they are bored 
        If their name starts with a 'b' then they are sad
    And then adds their name and friendliness to the dictionary
    if 
        1. their friendliness is greater than the friendliness of me
        2. they are happy. 
    """