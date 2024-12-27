
# The point here is you can cause an exception to occur
# raise Exception
# raise Exception("This exception occured! :(")
# raise ZeroDivisionError("This is weird right?")

try:
    # raise ZeroDivisionError("Custom Error!")
    print("This happens")
except ZeroDivisionError as division_error:
    print(division_error)
else:
    print("No error")
finally:
    print("Done")