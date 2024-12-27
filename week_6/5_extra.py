from matplotlib import pyplot as plt

# What types of plots can you create? How do you create them?
# What inputs into the plot function can you input? 
x_data: list[int] = [0, 1, 2]
y_data: list[int] = [1, 3, 2]
plt.plot(x_data, y_data, linestyle = "dotted", marker = "*")
# plt.show()

# What is the difference between a local and global variable?
# What defining feature makes them local vs global?

def add_three(x: str) -> str:
    return x + 3

output: type = add_three(10)
print(type(output))
print(output)

def power(a: float, x: float) -> float:
    return a ** x

def power_too(a: float, x: float = 2) -> float:
    return a ** x

print(power_too(3, 2))
print(power_too(3, 3))
print(power_too(3))
print(power_too(2))

# Do you know how to do a flow chart?
# What does each shape mean?
# Oval      - Start or End
# Rectangle - Modification of variables
# Parallellogram - Input from user or creation of varaibles
# Diamond   - Conditional (If statement or while loop) if arrows go down or while loop if arrow goes up

# The general ``Open a file'' algorithm
file_name: str = ""
try:
    with open(file_name, "r") as file:
        file_contents: str = file.read()
except FileNotFoundError:
    print("Couldn't open file")

# file_contents.split()
# analyse string file_contents
# remember you can always use .split(",") or .spilt(" ") or .split()

# When would you have to use operators?
# // would have to be used when you want to divide and output an integer
# % would have to be used whenever something is cyclic or checking divisibility

# while loop vs for loop, when should each be used?
