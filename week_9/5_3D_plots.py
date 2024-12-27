from matplotlib import pyplot as plt
import numpy as np

def main():
    
    x_quadratic: np.ndarray = np.linspace(-np.pi * 2, np.pi * 2)
    y_quadratic: np.ndarray = np.zeros(x_quadratic.shape)

    z_quadratic: np.ndarray = x_quadratic ** 2 - 1
    z_negative_quadratic: np.ndarray = -x_quadratic ** 2 + 1

    fig = plt.figure()

    ax = fig.add_subplot(projection = "3d")

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.plot(x_quadratic, y_quadratic, z_quadratic)
    ax.plot(x_quadratic, y_quadratic, z_negative_quadratic, linestyle = "--")


    plt.savefig("output/quadratic_3d_plot.png")

if __name__ == "__main__":
    main()
