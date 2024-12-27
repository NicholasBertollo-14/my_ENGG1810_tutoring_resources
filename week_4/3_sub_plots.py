from matplotlib import pyplot as plt
import math

# x and y positions for the sine function
sin_x_values: list[float] = [x / 10 for x in range(-100, 100, 1)]
sin_y_values: list[float] = []
for x_value in sin_x_values:
    sin_y_values.append(math.sin(x_value))

favourite_colours: dict[str: int] = {
    "Red": 0,
    "Green": 1,
    "Blue": 4
}

# fig and ax get decomposed, ax is a collection of 4 plots
fig, ax = plt.subplots(2, 2)
# fig is like the background
# ax is the axes, like the subplots, this is more useful
ax[0, 0].plot(sin_x_values, sin_y_values)
ax[0, 1].plot(sin_y_values, sin_x_values)
ax[1, 0].bar(favourite_colours.keys(), favourite_colours.values(), color = "hotpink", width = .95)
ax[1, 1].bar(favourite_colours.keys(), list(reversed(favourite_colours.values())), color = "hotpink", width = .95)

plt.show()

# Go onto revisions notes and show more functions