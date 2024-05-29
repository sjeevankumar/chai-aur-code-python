# Encapsulation
# Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

 
class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
    
    def get_brand(self):
        return self.__brand

    def set_brand(self,brand):
        self.__brand = brand
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

punch_ev = ElectricCar('TATA','Punch','220kWh')
print(punch_ev.set_brand('PUNCHEV'))
print(punch_ev.get_brand())