
def main():

    collection_A: list[str] = ["Nicholas", "Seth", "Alex", "Rowan", "Brandon"]
    collection_B: list[int] = [10, 5, 3, 4, 0]

    print("First")
    # Iterate over two iterables at once
    for a, b in zip(collection_A, collection_B):
        print(a, b)
    
    print("Second")
    # Using generators comprehension and zip
    for value_1, value_2 in zip((10 / x for x in range(1, 11)), (x / 10 for x in range(-10, 0))):
        print(value_1, value_2)
    
if __name__ == "__main__":
    main()
    