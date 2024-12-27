
# We want to open files. 
# This can be any file
# Let's print out my soup.txt

# Normal way
file_name: str = "soup.txt"
file = open(file_name, "r") # This is in read mode
print(file.read())
file.close()

# Better way
with open(file_name, "r") as orange:
    print(orange.read()) # automatically closes and don't have to worry

# What changes when I change this to "a" or "w"
# Who watched the lecture?
with open(file_name, "a") as file:
    file.write("This is a thing from Nicholas!\n")

# What happens if the file doesn't exist?
with open("orange.soup", "w") as file:
    file.write("This is a thing from Nicholas!\n")
    # print(file.read())

# Go onto the course notes and show more functions