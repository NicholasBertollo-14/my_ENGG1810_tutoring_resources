from scipy.optimize import curve_fit
import numpy as np
from random import random

def main():

    # Example in the tutorial
    fitting_data_to_the_curve()

    # Example that shows why
    finding_values_associated_with_a_function()

def general_cubic(x, a, b, c, d):
        return a * x ** 3 + b * x ** 2 + c * x + d

def fitting_data_to_the_curve():

    x_data = np.arange(0,3, 0.01)
    y_data = general_cubic(x_data, 3, 4, 2, 1) # this function represents the underlying non-linear trend
    # add a bit of random noise:
    for i in range(len(y_data)):
        y_data[i] += random() * 2 - 1 

    # Notice that this is a higher order function
    coeff = curve_fit(general_cubic, x_data, y_data)[0] # Returns a bunch of things, the answer is the zeroth thing
    # we expect the 4 coefficients to be close to 3,4,2,1
    print(f"Function coefficients a, b, c, d: {coeff}")

def exponential_model(x: float, a: float, b: float) -> float:
    return a * np.e ** (b * x)

def finding_values_associated_with_a_function():
    # Let's say we have some pretty random data that we think is exponential
    # Then we want to be able to interpolate by having a continuous function which
    # approximates the data. 
    x_data: np.ndarray = np.linspace(0, 10, 101)
    y_data: np.ndarray = np.sinh(x_data)

    values = curve_fit(exponential_model, x_data, y_data)[0]
    print(f"Values associated with the exponential are {values}")
     
if __name__ == "__main__":
    main()