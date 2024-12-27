
file_name: str = "numbers.txt"
# Binary mode!
with open(file_name, "rb") as my_file:
    print(my_file.read(10).decode("utf-8"))
    # This moved the cursor to position 10
    print(my_file.read(10).decode())
    # This moved the cursor even further

    # This is from the beginning of the file
    my_file.seek(3)
    print(my_file.tell())
    print(my_file.read().decode())

    # The second argument only works in binary mode
    # This is from the current position
    my_file.seek(3, 1)
    print(my_file.tell())
    print(my_file.read().decode())

    # This is from the end of the file
    my_file.seek(-3, 2)
    print(my_file.tell())
    print(my_file.read().decode())
    