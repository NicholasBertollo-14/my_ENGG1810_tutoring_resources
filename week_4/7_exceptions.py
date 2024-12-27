
# Planned exceptions usually occur when the error is within the hands of the user
# For example input from the user, or a file existing

file_name: str = "soupwefsdg.txt"
try:
    with open(file_name, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Couldn't find file :(")

