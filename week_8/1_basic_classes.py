
# This code defines a class called ClassName

# This is a class with the name ClassName
# Notice that with classes we use PascalCase instead of snake_case
class ClassName:

    # This is a constructor
    # This creates an object of this type
    def __init__(self):
        self.class_variable: str = "This is a variable assigned to the instance of the class (which is an object)"
    
    def my_method(self):
        print("This calls a method associated with the object")
        return self.class_variable

    # Any method (function) or variable that's associated with an object is called
    # an attribute, and therefore class_variable and my_method are both attributes.

# This code uses the class called ClassName
def main():
    my_class: ClassName = ClassName() # This calls the constructor of the class ClassName. 
    # I created an instance of ClassName called my_class
    print(my_class.class_variable) # This outputs the variable class_variable inside the class ClassName
    my_class.my_method() # This runs the method inside the class ClassName

if __name__ == "__main__":
    main()