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
    Make the number of intervals 1000
    Make show the function or turn it into a file, either is fine. 
    Use pandas to get the information from the file. 
    """

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
  