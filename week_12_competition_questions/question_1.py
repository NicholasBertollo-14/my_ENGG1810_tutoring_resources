
def we_dont_like_small_things(string: str) -> str:
    """
    returns a string which only contains letters
    where the ascii representation of the letter 
    (found using ord) is larger than 100.
    "hello" -> "hello"
    "zzaaaazzORANGE" -> "zzzz"
    """
