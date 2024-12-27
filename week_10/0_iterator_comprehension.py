
def main():
    # List and generator comprehension most important!

    # List comprehension
    # [output for input in iterable]
    print([value ** 2 for value in range(5)])

    # generator comprehension
    # (output for input in iterable)
    print((value ** 2 for value in range(3)))

    # Set comprehension
    # {output for input in iterable}
    print({value ** 2 for value in range(3)})

    # dictionary comprehension
    # {key_output: value_output for input in iterable}
    print({value: value ** 2 for value in range(3)})

if __name__ == "__main__":
    main()