from matplotlib import pyplot as plt
import numpy as np

def main():
    x_values: np.ndarray = np.linspace(-10, 10, 100)
    y_values: np.ndarray = x_values ** 2

    annotate_plot(x_values, y_values)
    xkcd_plot(x_values, y_values)
    easy_style_plot(x_values, y_values)
        
def annotate_plot(x_vals: np.ndarray, y_vals: np.ndarray):
    plt.plot(x_vals, y_vals) 

    plt.title("Plot with Annotation")
    plt.xlabel("x values")
    plt.ylabel("y values")

    turning_point: tuple[float, float] = (0, 0)
    plt.annotate("Turning Point", xy = turning_point, 
                 xytext = (turning_point[0], turning_point[1] + 20),
                 arrowprops = dict(facecolor='black', arrowstyle='->'))

    plt.grid()
    plt.show()
    plt.clf()

def xkcd_plot(x_vals: np.ndarray, y_vals: np.ndarray):
    plt.xkcd()

    plt.plot(x_vals, y_vals) 

    plt.title("Plot with XKCD")
    plt.xlabel("x values")
    plt.ylabel("y values")

    plt.grid()
    plt.show()
    plt.clf()

def easy_style_plot(x_vals: np.ndarray, y_vals: np.ndarray):
    # plt.xkcd()

    plt.plot(x_vals, y_vals, "g--") 
    plt.plot(x_vals, 1.6 ** x_vals, "b-")

    plt.title("Plot with XKCD")
    plt.xlabel("x values")
    plt.ylabel("y values")

    plt.grid()
    plt.show()
    plt.clf()

if __name__ == "__main__":
    main()