from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

def main():
    # Get the data (csv file) I chose a lazy dataset
    file: str = "sales_data_for_plotting.csv"
    df = pd.read_csv(file)
    
    # Put data in xcolumn df['X'] and ycolumn df['Y'] to the meshgrid
    revenue, expenses = np.meshgrid(df["Sales"], df["Expenses"])
    print(f"{revenue = }")
    print(f"{expenses = }")


    profit = revenue - expenses

    #create a figure (fig)
    fig = plt.figure()

    #You can add 3D subplot on the Axes(ax) 
    ax = fig.add_subplot(projection='3d')

    ax.set_xlabel("Revenue")
    ax.set_ylabel("Expenses")
    ax.set_zlabel("Profit") 

    ax.plot_surface(revenue, expenses, profit, cmap="hot")
    
    plt.savefig("output/profit_3d_csv_surface.png")

if __name__ == "__main__":
    main()