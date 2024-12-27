# Not examinable!
# NOTE: Not using good practices cause that's kinda the point of this file. 

# This is weird. I never recommend doing this
# However I wanted to show it, because it shows that
# classes are very similar to modules.
# They create their own scope, and are sorta similar to an inline import of a module (however I wouldn't think of them like this)
class Weird:
    print("This is inside a class, but not inside any sort of method?") # This line runs when it's created
    x: int = 10 # Where is this defined? It is assigned to the class or the instance of the class
    # If you're interested in this search up static variables in python
print("End of class definition")

# print(x) # x is not defined out here

# What constructor does this use?
weird_object: Weird = Weird() # We didn't define a constructor
print(weird_object.x)
print(Weird.x) # This is even weirder

