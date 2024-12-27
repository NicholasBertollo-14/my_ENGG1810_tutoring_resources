
def no_occurance(file_name: str, character: str) -> int:
    """
    Create a function which opens the file file_name and
    counts the number of times that character has occured 
    in the file. 
    If the file cannot be opened, print "{file_name} cannot be opened" and return -1.
    If the character is not a single character, then throw a ValueError with the error message
        "{character} is not a character!"
    """
    if len(character) != 1:
        raise ValueError(f"{character} is not a character!")
    
    try:
        with open(file_name, "r") as file_object:
            contents: str = file_object.read()
    except FileNotFoundError:
        print(f"{file_name} cannot be opened")
        return -1
    
    counter: int = 0
    for letter in contents:
        if letter == character:
            counter += 1
    return counter
    
        