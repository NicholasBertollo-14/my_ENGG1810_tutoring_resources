from scipy import optimize 
import math

def f(x: float) -> float:
    return (x + 4) * (x - 35)

def g(x: float) -> float:
    return math.sin(x ** 2)

def main():
    output = optimize.root(f, 0)
    print(f"{type(output)}")
    print(f"{output}")
    print(f"{output.x}")

    print(f"{optimize.root(f, 20) = }")
    print(f"{optimize.root(f, 20).x = }")

    print(f"{optimize.root(g, 20).x = }")
    print(f"{optimize.root(g, 0.2).x = }")

if __name__ == "__main__":
    main()