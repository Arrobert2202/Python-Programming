class Employee():
  def __init__(self, role, name, id):
    self.name = name
    self.role = role
    self.id = id

  def calculate_salary(self):
    pass

  def get_name(self):
    return self.name
  
class Manager(Employee):
  def __init__(self, name, id, base_salary, bonus, days_worked):
    super().__init__("manager", name, id)
    self.base_salary = base_salary
    self.bonus = bonus
    self.days_worked = days_worked

  def calculate_salary(self):
    return int((self.base_salary / 22) * self.days_worked + self.bonus)
  
  def assign_tasks_to_employees(self, nr_of_days):
    print(f"{self.name} is assigning new tasks for the employees. They have {nr_of_days} days to finish them.")

class Engineer(Employee):
  def __init__(self, name, id, base_salary, projects_finished_earlier, days_worked):
    super().__init__("Engineer", name, id)
    self.base_salary = base_salary
    self.pojects_finished_earlier = projects_finished_earlier
    self.days_worked = days_worked

  def calculate_salary(self):
    return int((self.base_salary / 22) * self.days_worked + (self.pojects_finished_earlier * 500))

  def write_code(self):
    print(f"{self.name} is writing code to finish the tasks.")
  
  def daily_meeting(self):
    print(f"{self.name} is attending a daily meeting.")

class Salesperson(Employee):
  def __init__(self, name, id, base_salary, days_worked, sales_number):
    super().__init__("Salesperson", name, id)
    self.base_salary = base_salary
    self.sales_number = sales_number
    self.days_worked = days_worked

  def calculate_salary(self):
    return int((self.base_salary / 22) * self.days_worked + (self.sales_number * 100))
  
  def client_discussion(self):
    print(f"{self.name} is attending a meeting with the client to discuss the project targets.")

manager = Manager("Ionut", 101, 7000, 3000, 20)
engineer = Engineer("Robert", 201, 5500, 3, 22)
salesperson = Salesperson("Elena", 301, 4250, 18, 15)

print(f"{manager.get_name()}'s salary is: {manager.calculate_salary()}$")
manager.assign_tasks_to_employees(7)
print()

print(f"{engineer.get_name()}'s salary is: {engineer.calculate_salary()}$")
engineer.daily_meeting()
engineer.write_code()

print()
print(f"{salesperson.get_name()}'s salary is: {salesperson.calculate_salary()}$")
salesperson.client_discussion()