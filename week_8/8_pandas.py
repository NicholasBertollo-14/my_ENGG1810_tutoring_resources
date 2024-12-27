import pandas as pd

def main():
    we_have_two_new_collections()
    # we_can_add_things()

def we_have_two_new_collections():
    # DataSeries is a collection which is strictly 1 dimensional. 
    # You can think about it as a column of a table. 
    # I would note that it has associated information with it
    # This is the reason it is useful.
    # Statistics are numbers in context.
    print("Part 1.1")
    students: list[str] = ["Paul", "Hamish", "Eileen", "Brian"]
    st_series: pd.Series = pd.Series(students) # This is a constructor for a Series Class
    print(f"{st_series}")
    print(f"{st_series[1] = }") # Numbers are used by default
    print(f"{st_series[2] = }")

    print("Part 1.2")
    # However this isn't the best way. You can add more context to the data. 
    # This give context to the names.
    st_series: pd.Series = pd.Series(students, index = ["Day 0", "Day 1", "Day 2", "Day 3"])
    print(f"{st_series}")
    print(f"{st_series['Day 1'] = }") # Notice that we aren't indexing by numbers anymore
    print(f"{st_series['Day 2'] = }")

    print("Part 1.3")
    weather: dict[str: str] = {"Day 1": "Sunny", "Day 2": "Rainy", "Day 3": "Cloudy"}
    weather_series: pd.Series = pd.Series(weather)
    print(f"{weather_series}")  
    print(f"{weather['Day 1'] = }")

    print("Part 2.1")
    # A DataFrame is a 2D DataSeries, DataSeries and DataFrames work nicely together. 
    # You can create a DataFrame out of multi dimensional dictionaries, or other multidimensional things. 
    grade: dict[str: dict[str: int]] = {
        "BTS_V":{
            "age": 25,
            "marks": 85
            },
        "Emma":{
            "age": 31,
            "marks": 91
            },
        "Spongebob":{
            "age": 25,
            "marks": 50
            }
    }
    df_grade: pd.DataFrame = pd.DataFrame(grade)
    print(df_grade)
    print(type(df_grade))

    # Think of loc as in the form:
    #   df_grade.loc[row_header] (DataSeries)
    #   df_grade.loc[[row_headers]] (DataFrame)
    #   df_grade.loc[:, column_header] (DataSeries)
    #   df_grade.loc[:, [column_headers]] (DataFrame)
    #   df_grade.loc[[row_headers], [column_headers]] (DataFrame)
    # Basically, if there is a list as input, it's a DataFrame, not a Series

    print("Part 2.2")
    # First
    print(df_grade.loc["age"])
    print(type(df_grade.loc["age"])) # This is a series when only getting 1

    print("Part 2.3")
    # Second
    print(df_grade.loc[["age", "marks"]]) # This gets two rows
    print(type(df_grade.loc[["age", "marks"]])) # This is a data frame

    print("Part 2.4")
    # Third
    print(df_grade.loc[:, "BTS_V"])
    print(type(df_grade.loc[:, "BTS_V"]))

    print("Part 2.5")
    # Fourth
    print(df_grade.loc[:, ["BTS_V"]])
    print(type(df_grade.loc[:, ["BTS_V"]]))

    print("Part 2.6")
    # Fifth
    print(df_grade.loc[["age", "marks"], ["BTS_V", "Emma"]])
    print(type(df_grade.loc[["age", "marks"], ["BTS_V", "Emma"]]))

def we_can_add_things():
    # Data!
    very_important_numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    more_very_important_numbers: list[int] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    # Series!
    very_important_numbers: pd.Series = pd.Series(very_important_numbers)
    more_very_important_numbers: pd.Series = pd.Series(more_very_important_numbers)

    # DataFrame!
    print(very_important_numbers * more_very_important_numbers)

if __name__ == "__main__":  
    main()