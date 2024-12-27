
# We talked about unary and binary operators when learning numpy
# I want to introduce the ternary operator
# The ternary operator is an inline if statement

# Notation:
# output_if_true if boolean_statement else output_if_false

# This is a number which is an integer
no_balloons: int = 11

print(no_balloons if no_balloons > 0 else 0)

print(f"We have {no_balloons} balloons" if no_balloons > 0 else "We have no balloons")

# Don't abuse it too much
print(10 if no_balloons > 10 else 0 if no_balloons < 0 else no_balloons)