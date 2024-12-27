from time import process_time
from matplotlib import pyplot as plt

def main():
    # time_square()
    time_fib()

def time_square():
    start_time: float = process_time()
    square_list(list(range(100000000)))
    end_time: float = process_time()
    print(f"Total Time: {end_time - start_time}")

def square_list(values: list[float]) -> list[float]:
    new_values: list[float] = []
    for value in values:
        new_values.append(value ** 2)
    return value

# With reference to the graph, why do we call fibonacci
# a exponential-time algorithm
def time_fib():
    times: list[float] = []
    for i in range(40):
        start_time: float = process_time()
        fibonacci(i)
        times.append(process_time() - start_time)
    
    plt.plot(times)
    plt.show()
    plt.savefig("output/fib_time.png")

# Don't worry about using fibonacci inside fibonacci
# This is called recursion. 
def fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    main()