# Note for Nicholas next year, add f strings to tell where things come from

my_global_variable: int = 100
print(f"{my_global_variable = }")

# You can think of the inside of a function as a special place
# that is within it's own bubble
# It knows things exists that it can use, but when something
# happens inside, this is only known locally
def local_variable_example_function():
    # print(my_global_variable)
    my_local_variable: int = 10
    return my_local_variable

# print(my_local_variable)

# As you can tell we can access global variables inside a function 
# However we cannot modify it!
# In fact in the example below, if it can tell that you're modifying it
# Then it assumes it's a local variable
def can_we_access_a_global_variable_inside_a_function():
    print(f"We can access a global variable inside: {my_global_variable = }, but we cannot modify")
    # my_global_variable += 1

can_we_access_a_global_variable_inside_a_function()

# However we can modify it if we use the global keyword!
def this_pushes_global_variable_inside_for_a_second():
    global my_global_variable
    print(f"But we can modify if we use the global keyword: {my_global_variable = }")
    my_global_variable += 1

this_pushes_global_variable_inside_for_a_second()

def is_this_global_or_local():
    # my_global_variable: int = 69
    print(f"Global or Local?: {my_global_variable}")

is_this_global_or_local()
print(f"{my_global_variable = }")

def what_about_this():
    my_global_variable: int = 420
    # my_global_variable += 1
    print(f"What about this: {my_global_variable = }")

what_about_this() # It has the same name but is local!
print(f"{my_global_variable = }")

# Using the global keyword can also create a global variable inside a function
# I don't know why you would ever want to do this, however you can
def can_we_create_a_global_variable_inside_a_function():
    global a_global_variable_inside_a_function
    a_global_variable_inside_a_function = 10
    print(f"Creating a global variable in a function: {a_global_variable_inside_a_function}")

can_we_create_a_global_variable_inside_a_function()
print(a_global_variable_inside_a_function)

a_global_variable_inside_a_function += 1
print(a_global_variable_inside_a_function)

can_we_create_a_global_variable_inside_a_function()
print(a_global_variable_inside_a_function)