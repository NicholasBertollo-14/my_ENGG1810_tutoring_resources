from matplotlib import pyplot as plt
import re
import numpy as np
from scipy import interpolate
import pandas as pd

def plot_change(name: str, values: list[float]):
    """
    Plot the values on a graph. 
    Plot the change in the values on the graph. 
    the x-values should be the index. 
    The last value should be the same as the second last value. 
    E.g. [1, 2, 1, 4, 5] should map this and [1, -1, 3, 1, 1]
    Note: create a png called {name}.png 
    """
    change: list[float] = []
    for index, value in enumerate(values[:-1]):
        change.append(values[index + 1] - value)
    change.append(change[-1])

    plt.plot(values)
    plt.plot(change)
    plt.grid()
    plt.savefig(f"{name}.png")

def redact(file_name: str):
    """
    If the file cannot be opened then return
    If the file can be opened then write to the file
    the contents with the file, however every time there exists a number, 
    this is replaced with "XXX". 
    Note that this is the whole number, not single digit. 
    So hello 11 33333 -> hello XXX XXX
    Use the re library for this task. 
    """
    # Let's open the file, then use re.sub, then write to the file
    try:
        with open(file_name, 'r') as document:
            content: str = document.read()
    except FileNotFoundError:
        print("Could not open file.")
        return
    
    content: str = re.sub("[1-9]+", "XXX", content)
    print(content)
    with open(file_name, 'w') as document:
        document.write(content)

def csv_interpolate_w_pandas(csv_file_name: str):
    """
    Create a function, which opens the file csv_file_name
    If this can't be done then print a message and return
    Once open, each row represents a point in 2D. 
    For example the file might look like this:
        x_values, y_values
        1,5
        2,4
        3,3
        4,2
        5,1
    Use cubic_spline interpolation on these points
    and plot the resulting value. 
    Use pandas to get the information from the file. 
    """
    information: pd.DataFrame = pd.read_csv(csv_file_name)

    interpolated_function: function = interpolate.CubicSpline(information.loc[:, "x_values"], information.loc[:, "y_values"])

    amount_of_intervals: int = 1000
    x_values: np.ndarray = np.linspace(min(information.loc[:, "x_values"]), max(information.loc[:, "x_values"]), amount_of_intervals)
    y_values: np.ndarray = interpolated_function(x_values)

    plt.plot(x_values, y_values)
    plt.show()

def csv_interpolate(csv_file_name: str):
    """
    Create a function, which opens the file csv_file_name
    If this can't be done then print a message and return
    Once open, each row represents a point in 2D. 
    For example the file might look like this:
        x_values, y_values
        1,5
        2,4
        3,3
        4,2
        5,1
    Use cubic_spline interpolation on these points
    and plot the resulting value. 
    Use pandas to get the information from the file. 
    Do not use pandas whatsoever!
    """
    try:
        with open(csv_file_name, 'r') as document:
            content: str = document.read()
    except FileNotFoundError:
        print("Could not open the file!")
        return

    lines: list[str] = content.split('\n')
    x_values: list[float, float] = []
    y_values: list[float, float] = []
    for line in lines[1:]: # Skipping the first line.
        line: str = line.split(',')
        try:
            x_values.append(float(line[0].strip()))
            y_values.append(float(line[1].strip()))
        except:
            print("Not a number")
            return
    x_values: np.ndarray = np.array(x_values)
    y_values: np.ndarray = np.array(y_values)
    
    interpolated_function: function = interpolate.CubicSpline(x_values, y_values)

    amount_of_intervals: int = 1000
    x_values: np.ndarray = np.linspace(min(x_values), max(x_values), amount_of_intervals)
    y_values: np.ndarray = interpolated_function(x_values)

    plt.plot(x_values, y_values)
    plt.show()