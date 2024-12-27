
print("#1")
# We already know basic exceptions
try:
    with open("file.txt", "r") as my_file:
        print(my_file.read())
except FileNotFoundError:
    print("The file didn't exist")

print("#2")
# This is only a single type of exception however, there are more
# TypeError, ValueError, IndexError, SyntaxError
try:
    # print(1 / 0) # This is still an error
    print("Hi" + 3)
except TypeError:
    print("Wrong type!")

print("#3")
# You can also get the name of the error
try:
    print("Hi" + 3)
except TypeError as my_error:
    print(f"{my_error}") 
    # Notice it doesn't print the error type, just the message

print("#4")
# You can also catch multiple exceptions if you want
try:
    with open("file.txt", "r") as my_file:
        for character in my_file:
            if character.isnumeric():
                print(100 / int(character))
except FileNotFoundError as file_no_exist:
    print(f"No File! {file_no_exist}")
except ZeroDivisionError:
    print(f"You divided by zero!")

print("#5")
# You can even do this in the same line
try:
    with open("file.txt", "r") as my_file:
        for character in my_file:
            if character.isnumeric():
                print(100 / int(character))
except (FileNotFoundError, ZeroDivisionError) as an_error:
    print(f"An error you expected occured: {an_error}")

print("#6")
# You can even add an else block to the end if you want
# This occurs if an error didn't occur
try:
    if "a":
        print(1/0)
except ZeroDivisionError:
    print("Division by 0!")
else:
    print("No division by 0!")

print("#7")
# Finally keyword is a block which occurs irrespective of 
# Whether an error occured or not
try:
    print(1/0)
except ZeroDivisionError:
    print("You divided by zero :(")
finally:
    print("We cry :(")

print("#8")
# You can put both together, put else first
try:
    pass
    # print(1/0)
except ZeroDivisionError:
    print("You divided by zero :(")
else:
    print("There was no error! :)")
finally:
    print("We cry :(")

print("#9")
# The exception Hierachy!
# ZeroDivisionError -> ArithmeticError -> Exception -> BaseException
# Put the least general first

# This is bad because ZeroDivisionError will never occur
try:
    x: float = 1 / 0
except Exception:
    print("There was an exception")
except ZeroDivisionError:
    print("There was a zero division error!")

print("#10")
# This is a basic example
def bmi_calculator(height, weight):
    height = height * 0.01
    bmi = weight / (height * height)
    return bmi 

try:
    height: float = float(input("Enter your height (cm)):"))
    weight: float = float(input("Enter your weight (kg):"))
except ValueError as error:
    print(f"Error! please enter a valid number. {error}") 
else:
    bmi: int = round(bmi_calculator(height, weight),3)
    print(f"Your body mass index is {bmi}")

