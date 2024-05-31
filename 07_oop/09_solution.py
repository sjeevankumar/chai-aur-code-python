# Class Inheritance and isinstance() function
# Demonstarte the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar

class Car:
    total_cars = 0
    
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        Car.total_cars+=1
        
    def get_brand(self):
        return self.__brand
    
    def set_brand(self,brand):
        self.__brand = brand
    
    def full_name(self):
        return f'{self.__brand } {self.model}'

    def fuel_type(self):
        return 'Petrol or Diesel'

    @staticmethod
    def general_description():
        return 'Cars are means of transport'
    
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return 'Electric charge'
    

my_tesla = ElectricCar('Tesla','Model S','85kWh')
print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar))
