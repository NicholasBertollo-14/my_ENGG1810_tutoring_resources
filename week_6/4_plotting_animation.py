from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# This is just getting a bunch of points to plot
sin_x: list[float] = [x / 10 for x in range(-31, 32)] # Do not worry about this notation
sin_y: list[float] = [math.sin(x) for x in sin_x] # This is simply x values and y values of the sine function

epsilon: float = 0.1 # I use this to make the top and bottom of the graph nicer

# Let's use subplots
fig, ax = plt.subplots() # When nothing is input it's a subplot with a single plot
ax.grid()
ax.set_xlim(min(sin_x), max(sin_x)) 
ax.set_ylim(min(sin_y) - epsilon, max(sin_y) + epsilon)
# line, = ax.plot([], [])
line = ax.plot([], [])[0]

# This is all new! We can add the animation to our data
# At the beginning of the animation we need something
def init():
    line.set_data([], [])
    return line

# Think of t as time
def animate(t: int):
    line.set_data(sin_x[:t + 1], sin_y[:t + 1]) # Remember it doesn't include t + 1
    return line

# This is important
# We are using functions as variables
# This is called higher order functions
# We are also putting all this information into this weird function
# This isn't actually a function, it's a constructor
# This creates a new object that we can manipulate 
anim = FuncAnimation(fig, animate, init_func = init, frames = len(sin_x), interval = 50)
anim.save("sine.gif")