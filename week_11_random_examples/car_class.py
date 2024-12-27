

class Car:
    def __init__(self, brand: str, colour: str, price: float):
        self.brand: str = brand
        self.colour: str = colour
        self.fuel_litres: float = 50
        self.price: float = price
    
    def drive(self, hours_driven: float):
        factor_depreciation_per_hour: float = 0.001
        fuel_used_per_hour: float = 12

        litres_used: float = fuel_used_per_hour * hours_driven
        if litres_used > self.fuel_litres:
            raise Exception("Cannot drive that long!")

        self.fuel_litres -= fuel_used_per_hour * hours_driven

        self.price *= (1 - factor_depreciation_per_hour) ** hours_driven
    
