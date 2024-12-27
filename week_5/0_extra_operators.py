

# The ``is'' keyword
a: int = 10
b: int = 10
print(f"{(a == b) = } vs {(a is b) = }")

x: list[int] = [1, 2, 3]
y: list[int] = [1, 2, 3]
print(f"{(x == y) = } vs {(x is y) = }")

# But why is this the case?
print(f"a's id is {id(a)} and b's is {id(b)}")
print(f"x's id is {id(x)} and y's is {id(y)}")

# a is b this is the same as id(a) == id(b)

# The None type
print(type(None))
print(None)

# print(print("Hello"))

# The ``in'' keyword
# This has two uses:
#   for loops
#   checking containment

# For loop example of in
for i in [1, 2, 3]:
    # This is looping
    pass

# if statement example of in
if 1 in [1, 2, 3]:
    print("1 is in [1, 2, 3]")

# list slices
my_list: list[int] = [0, 1, 2, 3, 4, 5]
print(my_list[1:4])
print(my_list[0:4])
print(my_list[3:])
print(my_list[:2])
print(my_list[0:6])