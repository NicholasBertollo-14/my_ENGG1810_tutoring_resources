import matplotlib.pyplot as plt
import pandas as pd
from scipy import interpolate
import numpy as np
from typing import Callable

file_name: str = "sales_data_for_plotting.csv"

def main():
    linear_interpolation()
    cubic_spline_interpolation()

def linear_interpolation():
    df_sales: pd.DataFrame = pd.read_csv(file_name)
    fig, ax = plt.subplots()
    ax.plot(df_sales["Year"], df_sales["Profit"], "ro") # red, circles

    # This is the important line, everything else you've seen
    interpolated_function: Callable[[float], float] = interpolate.interp1d(df_sales["Year"], df_sales["Profit"])

    x_est = np.linspace(min(df_sales["Year"]), max(df_sales["Year"]), 30)
    y_est = interpolated_function(x_est)
    ax.plot(x_est, y_est, "b--")


    ax.set_xlabel("Year")
    ax.set_ylabel("Profit ($)")
    plt.savefig("output/sales_data_linear.png")
    plt.clf()

def cubic_spline_interpolation():

    df_sales: pd.DataFrame = pd.read_csv(file_name)
    fig, ax = plt.subplots()
    ax.plot(df_sales["Year"], df_sales["Profit"], "ro") # red, circles

    # This is the important line, everything else you've seen
    interpolated_function: Callable[[float], float] = interpolate.CubicSpline(df_sales["Year"], df_sales["Profit"])

    x_est = np.linspace(min(df_sales["Year"]), max(df_sales["Year"]), 30)
    y_est = interpolated_function(x_est)
    ax.plot(x_est, y_est, "g--")


    ax.set_xlabel("Year")
    ax.set_ylabel("Profit ($)")
    plt.savefig("output/sales_data_cubic.png")
    plt.clf()

if __name__ == "__main__":
    main()