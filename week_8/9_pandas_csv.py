import pandas as pd
import matplotlib.pyplot as plt

def main():
    file_name: str = "sales_data_for_plotting"

    # Load the CSV file
    df: pd.DataFrame = pd.read_csv(file_name + ".csv")
    print(df)

    # Plot Sales, Expenses, and Profit over the Years
    df.plot(x = "Year", y = ["Sales", "Expenses", "Profit"])
    plt.title("Company Sales, Expenses, and Profit Over Time")
    plt.ylabel("Amount in $")
    plt.xlabel("Year")
    plt.savefig(file_name)

if __name__ == "__main__":
    main()

# Point: pandas and matplotlib are best friends!
