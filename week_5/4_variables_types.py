
# There are pass by value types and pass by reference types
# All variables are pass by reference other than:
#   int, float, str, bool, complex
# So basically your normal types

# You will notice different behaviour when inputting things into functions
# This function uses a pass by value type (int) and is trying to change it in place
def perform_int_operation_in_place(local_int: int):
    local_int += 1

my_int: int = 10
perform_int_operation_in_place(my_int)
print(my_int)

# This function uses a pass by reference type (list) and changes it in place
def perform_list_operation_in_place(local_list: list):
    local_list.append(10)

my_list: list = ["Hello World!"]
perform_list_operation_in_place(my_list)
print(my_list)

