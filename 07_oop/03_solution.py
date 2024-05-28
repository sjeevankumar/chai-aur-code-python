# Inheritance
# Create an ElectricCar class that inherits from the Car class and has an additional attribute batter_size.

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

punch_ev = ElectricCar('TATA','Punch','220kWh')
print(punch_ev.full_name())
    