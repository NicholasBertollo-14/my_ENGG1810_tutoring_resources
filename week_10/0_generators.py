
def main():
    print("First:")
    for i in my_range(0, 5, 2):
        print(i)
    
    print("Second:")
    for i in concat([[1, 2, 3, 4, 5], [6, 7, 8], [9, 10]]):
        print(i)

# A generator is simiar to a iterator in that it is
# iterable (can be put in a for loop)
# However it is not a collection
# And intead stores a rule for what the next value is

# Here is range generator
def my_range(start: int = 0, stop: int = 0, step: int = 0):
    index: int = start
    while index < stop:
        yield index
        index += step

# Here is a list that generates the next thing in a list of lists
# e.g. [[1, 2], [3]] will output 1, 2, then 3
def concat(list_of_lists: list[list[any]]):
    for inner_list in list_of_lists:
        for value in inner_list:
            yield value

if __name__ == "__main__":
    main()

