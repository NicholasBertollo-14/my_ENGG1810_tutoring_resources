
# It's important to recognise that errors happen for different reasons
# There are 3 reasons in fact:
#   Syntax Error - Your syntax is wrong
#   Runtime Error - Something went wrong when the program ran
#   Logical Error - The output of the program is wrong

# These are in order of horrible-ness and it's important to understand how to fix them

# Syntax Error
for i in range(10):
    # x: int = "Hello my name is +" i
    # print(x)
    pass

# Runtime Error
for word in "Hello my name is nicholas! ".split(" "):
    if word != "":
        print(word[0])

import math

# Logical Error
vector: list[float] = [1, 2, 3, 4, 5]
magnitude: float = 0
for number in vector:
    # We want to find the magnitude of the vector
    magnitude += number ** 3
magnitude = math.sqrt(magnitude)
print(magnitude)

# Tips:
# If has not been obvious, USE PRINT STATEMENTS TO DEBUG!
# If you need information, then print it out!
# If you don't understand how a function works
#   print input and output
#   go onto the notes and research
#   research by going online or ask on ed
# YOU CANNOT TYPE CODE IF YOU DON'T UNDERSTAND THE PROBLEM YOU'RE TRYING TO SOLVE
# There is a certain number of problem solving techniques that you have built up:
#   Categorise the problem
#   Guess and research which functions you will use
#   Write out or develop a high level algorithm to solve it
#   Use pattern recognition to tell you important things about it
#   What information do you have, what information do you need?
#   Where are you going to store this information?
#   How will it be stored?
#   What data type is appropriate?
# YOU HAVE MANY TOOLS AT YOUR DISPOSAL, USE THEM!
