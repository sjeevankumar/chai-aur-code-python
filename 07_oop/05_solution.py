# Polymorphism
# Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes,but with different behaviors

class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        
    def get_brand(self):
        return self.__brand
    
    def set_brand(self,brand):
        self.__brand = brand
    
    def full_name(self):
        return f'{self.__brand } {self.model}'

    def fuel_type(self):
        return 'Petrol or Diesel'

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return 'Electric charge'
    
maruthi = Car('Maruthi','Suzuki')
print(maruthi.fuel_type())

punch_ev = ElectricCar('TATA','PUNCH','290kWh')
print(punch_ev.fuel_type())

    
    