
class Polynomial:
    # Question: What is self?
    def __init__(, name_of_polynomial: str, coefficients: list[float]):
        self.name: str = name_of_polynomial # How is self used here?
        self.coefficients: list[float] = coefficients # [3, 2, 1] => 3 x^2 + 2 x + 1
    
    # What happens if I don't input self into the method?
    def get_name(self) -> str:
        return self.name
    
    # Why do we use getters and setters instead of accessing a value directly?
    # Why is this good practice?
    def set_name(self, new_name: str):
        self.name: str = new_name

    def get_coefficients(self) -> list[float]:
        return self.coefficients
    
    # What does this method do?
    def add_to_coefficients(self, coefficients_to_add: list[float]):
        if len(coefficients_to_add) == len(self.coefficients):
            for index, coefficient in enumerate(coefficients_to_add):
                self.coefficients[index] += coefficient  

    # What does this method do?
    def evaluate(self, x: float) -> float:
        output: float = 0
        for power, coefficient in enumerate(reversed(self.coefficients)):
            output += coefficient * (x ** power)
        return output

    # Do not worry about this, this just defines how it should be casted to a string
    def __str__(self) -> str:
        return f"{self.name}: {self.coefficients}" 
    
    def __repr__(self) -> str:
        return str(self)

def main():
    cubic_polynomial: Polynomial = Polynomial("Cubic", [4, 3, 2, 1])
    print(cubic_polynomial)
    print(cubic_polynomial.get_name())
    print(cubic_polynomial.get_coefficients())
    print(cubic_polynomial.evaluate(2))

    linear_polynomial: Polynomial = Polynomial("Linear", [2, 1])
    print(linear_polynomial)
    print(linear_polynomial.get_name())
    print(linear_polynomial.get_coefficients())
    print(linear_polynomial.evaluate(2))

    # Let's say we want to change the name of the polynomial
    linear_polynomial.set_name("Slow growing linear polynomial that adds 2 and is initially 1")
    print(linear_polynomial)

    # Or what if we want to add to a polynomial
    linear_polynomial.add_to_coefficients([1, -1])
    print(linear_polynomial)

if __name__ == "__main__":
    main()