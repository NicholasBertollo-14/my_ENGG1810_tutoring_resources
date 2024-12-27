# Do this only if you have time


# This here is extra content which is basically quality of life
# Explain the true meaning of ``object''
# Explain that a function is simply an object
# Explain that you can treat a function as an object
# Therefore you can input a function into a function

# map is a function which performs a function on a list
def square(x: float) -> float:
    return x ** 2

print(type(square))
print(square)

my_list: list[float] = [1, 2, 3, 4, 5, 6]
# Why doesn't it output a list???
print(map(square, my_list))
print(list(map(square, my_list)))

# def my_map():
#     def inner_function():
#         print("Hi")
#     return inner_function