
def no_occurance(file_name: str, character: str) -> int:
    """
    Create a function which opens the file file_name and
    counts the number of times that character has occured 
    in the file. 
    If the file cannot be opened, print "{file_name} cannot be opened" and return -1.
    If the character is not a single character, then throw a ValueError with the error message
        "{character} is not a character!"
    """
    
    try:
        with open(file_name, 'r') as file_object:
            file_contents: str = file_object.read()
    except FileNotFoundError:
        print(f"{file_name} cannot be opened")
        return -1
    
    if len(character) != 1:
        raise ValueError(f"{character} is not a character!")
    
    counter: int = 0
    for letter in file_contents:
        if character == letter:
            counter += 1
    return counter

def we_dont_like_small_things(string: str) -> str:
    """
    returns a string which only contains letters
    where the ascii representation of the letter 
    (found using ord) is larger than 100.
    "hello" -> "hello"
    "zzaaaazzORANGE" -> "zzzz"
    """
    return_string: str = ''
    for letter in string:
        if ord(letter) > 100:
            return_string += letter
    return return_string

def flatten(list_of_lists: list[list[any]]) -> list[any]:
    """
    flattens a list of lists into a list in order
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]] -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    return_list: list[any] = []
    for inner_list in list_of_lists:
        for value in inner_list:
            return_list.append(value)
    return return_list

def average(values: set[float]) -> float:
    """
    Calculates the average of the numbers input
    return 0 is the set is empty
    """
    if len(values) == 0:
        return 0
    sum_of_values: float = 0
    for value in values:
        sum_of_values += value
    return sum_of_values / len(values)

def variance(values: set[float]) -> float:
    """
    Calculates the variance of the numbers input.
    Use the average function above.
    Formula is online by typing `sample variance`
    or on the other slide. 
    return 0 if the set is it contains less than 2 items
    """
    if len(values) < 2:
        return 0
    average_of_values: float = average(values)
    sum_of_squares: float = 0
    for value in values:
        sum_of_squares += (value - average_of_values) ** 2
    return sum_of_squares / (len(values) - 1)

class Person:
    def __init__(self, name: str, friendliness: int):
        """
        A person has the attributes name and friendliness
        """
        self.name: str = name
        self.friendliness: int = friendliness
    
    def interaction(self, mood: str):
        """
        Will change friendliness by mood.
        If their mood is "happy" then increase friendliness by 10
        If their mood is "bored" then decrease friendliness by 3
        If their mood is "sad" then decrease friendliness by 10
        """
        if mood == "happy":
            self.friendliness += 10
        elif mood == "bored":
            self.friendliness -= 3
        elif mood == "sad":
            self.friendliness -= 10
    
def invite_to_party(me: Person, friends: set[Person]) -> dict[str, int]:
    """
    This function performs an interaction with every person
        If their name starts with an 'a' then they are happy
        If their name starts with a 'b' then they are bored
        If their name starts with a 'c' then they are sad 
        skip over any friend that doesn't start with either of these letters
    And then adds their name and friendliness to the dictionary
    if 
        1. their friendliness is greater than the friendliness of me
        2. they are happy. 
    """
    friends_to_invite: dict[str, int] = {}
    for friend in friends:
        
        if friend.name == '':
            continue

        if friend.name[0] == 'a':
            friend.interaction("happy")
        elif friend.name[0] == 'b':
            friend.interaction("bored")
        elif friend.name[0] == 'c':
            friend.interaction("sad")
        else:
            continue
        
        if friend.friendliness > me.friendliness and friend.name[0] == 'a':
            friends_to_invite[friend.name] = friend.friendliness