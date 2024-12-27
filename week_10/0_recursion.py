
def main():
    for i in range(10):
        print(factorial(i))

    for i in range(10):
        print(fibonacci(i))
    
    print(fibonacci(40))

# Factorial
# 0! = 1
# n! = n * (n - 1)!

# Function which finds the factorial of a number
def factorial(n: int) -> int:
    # By definition
    if n == 0:
        return 1
    elif n > 0:
        return n * factorial(n - 1)

# Function which finds the nth fibonacci number
def fibonacci(n: int) -> int:
    # By definition
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    main()