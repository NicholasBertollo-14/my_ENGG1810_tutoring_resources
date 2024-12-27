
# Is a tuple defined by the parentheses?
my_tuple: tuple[int] = (1, 2, 3)
other_tuple: tuple[int] = 1, 2, 3

# Decompose or unpacking
a, b, c = my_tuple
print(f"{a=}, {b=}, {c=}")