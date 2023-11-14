class Vehicle():
  def __init__(self, make, model, year):
    self.__make = make
    self.__model = model
    self.__year = year

  def get_make(self):
    return self.__make
  
  def get_model(self):
    return self.__model
  
  def get_year(self):
    return self.__year
  
class Car(Vehicle):
  def __init__(self, make, model, year, fuel_capacity, fuel_efficiency):
    super().__init__(make, model, year)
    self.__fuel_capacity = fuel_capacity
    self.__fuel_efficiency = fuel_efficiency
  
  def calculate_mileage(self):
    return (self.__fuel_capacity / self.__fuel_efficiency) * 100
  
class Motorcycle(Vehicle):
  def __init__(self, make, model, year, fuel_capacity, fuel_efficiency):
    super().__init__(make, model, year)
    self.__fuel_capacity = fuel_capacity
    self.__fuel_efficiency = fuel_efficiency
  
  def calculate_mileage(self):
    return (self.__fuel_capacity / self.__fuel_efficiency) * 100
  
class Truck(Vehicle):
  def __init__(self, make, model, year, engine_power):
    super().__init__(make, model, year)
    self.engine_power = engine_power

  def calculate_towing_capacity(self):
    if self.engine_power < 300:
      return self.engine_power * 3
    else: return self.engine_power * 2

car = Car("Audi", "RS7", 2023, 50, 13)
print(f"{car.get_make()} {car.get_model()} made in {car.get_year()} has a mileage of {car.calculate_mileage():.2f} miles per gallon.")

motorcycle = Motorcycle("Harley", "Davidson", 2015, 30, 7)
print(f"{motorcycle.get_make()} {motorcycle.get_model()} made in {motorcycle.get_year()} has a mileage of {motorcycle.calculate_mileage():.2f} miles per gallon.")

truck = Truck("Ford", "F-150", 2020, 278)
print(f"{truck.get_make()} {truck.get_model()} made in {truck.get_year()} has a towing capacity of {truck.calculate_towing_capacity()} pounds.")