from matplotlib import pyplot as plt
import numpy as np
from typing import Callable

def main():
    plot_sin(100)
    
    plot_func(np.sqrt, 0, 100, "square_root", 1000)
    plot_func(np.sin, -np.pi, np.pi, "sine_but_better")

# This is neccessary for this part of the unit
def plot_sin(clarity: int = 100):
    # This is a valid use of raise
    if clarity < 4: 
        raise ValueError("Yeah Nah Bro")
    sin_x: np.ndarray = np.linspace(-np.pi, np.pi, clarity)
    sin_y: np.ndarray = np.sin(sin_x) # Look how easy this was; np.sin is a unary function

    # Using subplots like usual
    fig, ax = plt.subplots()
    ax.grid()
    ax.set_xlim(min(sin_x), max(sin_x))
    ax.set_ylim(min(sin_y), max(sin_y))
    
    # numpy and matplotlib are best friends!
    ax.plot(sin_x, sin_y)
    fig.savefig("sine.png")

# This here is not needed, but it's sexy
def plot_func(function_to_plot: Callable[[float], float], lower_bound: float, upper_bound: float, name: str = "function", clarity: int = 100):
    if clarity < 4 or lower_bound >= upper_bound: 
        raise ValueError("Yeah Nah Bro")
    x_vals: np.ndarray = np.linspace(lower_bound, upper_bound, clarity)
    y_vals: np.ndarray = function_to_plot(x_vals) # Look how easy this was np.sin is a unary function

    epsilon: float = 0.1
    epsilon_x: float = min((epsilon * abs(max(x_vals) - min(x_vals)), 1))
    epsilon_y: float = min((epsilon * abs(max(y_vals) - min(y_vals)), 1))

    fig, ax = plt.subplots()
    ax.grid()
    ax.set_xlim(min(x_vals) - epsilon_x, max(x_vals) + epsilon_x)
    ax.set_ylim(min(y_vals) - epsilon_y, max(y_vals) + epsilon_y)
    ax.plot(x_vals, y_vals, color = "purple")
    fig.savefig(f"{name}.png")

if __name__ == "__main__":
    main()