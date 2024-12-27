from matplotlib import pyplot as plt
import math
import sys

# This is how a math function works
# print(math.sin(math.pi / 2)) # 1 by unit circle

sin_x_values: list[float] = [x / 10 for x in range(-100, 100, 1)]
sin_y_values: list[float] = []
for x_value in sin_x_values:
    sin_y_values.append(math.sin(x_value))

plt.plot(sin_x_values, sin_y_values)
plt.grid()
plt.title("Sinoisoidal Function")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.savefig("output/sine_function.png")

plt.clf() # Special function to clear the plot

# Input some argument as command line
colour_tallies: list[int] = sys.argv[1:]
if len(colour_tallies) == 0: 
    colour_tallies = [1, 2, 3]
# Create dictionary dependant on this
favourite_colours: dict[str: int] = {
    "Red": colour_tallies[0],
    "Green": colour_tallies[1],
    "Blue": colour_tallies[2]
}

# Create a bar chart
plt.bar(favourite_colours.keys(), favourite_colours.values(), color = "hotpink", width = .95)
plt.title("ENGG1810 Favourite Colours")
plt.xlabel("Colours")
plt.ylabel("Tally")
plt.show()