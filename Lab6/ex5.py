class Animal():
  def __init__(self, species, age, sound):
    self.species = species
    self.age = age
    self.sound = sound
  
  def get_species(self):
    return self.species
  
  def get_age(self):
    return self.age
  
  def make_sound(self):
    print(self.sound)
  
class Mammal(Animal):
  def __init__(self, species, age, sound, hair_color):
    super().__init__(species, age, sound)
    self.hair_color = hair_color

  def get_hair_color(self):
    return self.hair_color
  
  def walk(self):
    print(f"{self.get_species()} is walking")

class Bird(Animal):
  def __init__(self, species, age, sound, migratory, wingspan):
    super().__init__(species, age, sound)
    self.migratory = migratory
    self.wingspan = wingspan

  def fly(self):
    print(f"{self.get_species()} is flying")
  
  def is_migratory(self):
    if self.migratory:
      print(f"{self.species} is migratory")
    else:
      print(f"{self.species} is not migratory")

  def get_wingspan(self):
    return self.wingspan
  
class Fish(Animal):
  def __init__(self, species, age, sound, environment, diet):
    super().__init__(species, age, sound)
    self.environment = environment
    self.diet = diet

  def swim(self):
    print(f"{self.get_species()} is swimming")

  def get_environment(self):
    print(f"{self.species} lives in {self.environment}")
  
  def get_diet(self):
    print(f"{self.species} is {self.diet}")

mammal = Mammal("Tiger", 3, "Roar", "Orange")
print(f"Species: {mammal.get_species()}\nAge: {mammal.get_age()}\nHair-Color: {mammal.get_hair_color()}")
mammal.walk()
mammal.make_sound()
print()

bird = Bird("Eagle", 2, "Screech", True, 6)

print(f"Species: {bird.get_species()}\nAge: {bird.get_age()}\nWingspan: {bird.get_wingspan()}")
bird.is_migratory()
bird.fly()
bird.make_sound()
print()

fish = Fish("Salmon", 1, "Splash", "River", "Omnivorous")

print(f"Species: {fish.get_species()}\nAge: {fish.get_age()}")
fish.get_environment()
fish.get_diet()
fish.swim()
fish.make_sound()