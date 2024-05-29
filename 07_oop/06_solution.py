# Class Variables
# Add a class variable to Car that keeps track of the number of cars created

class Car:
    total_cars = 0
    
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        Car.total_cars+=1
        
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
    
Car('Maruthi','Suzuki')
ElectricCar('TATA','PUNCH','290kWh')

print(Car.total_cars)