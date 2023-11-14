class Account():
  def __init__(self, balance = 0):
    self.balance = balance

  def withdraw(self, amount):
    if self.balance < amount:
      print("You don't have enough money")
    else:
      self.balance -= amount
      print("Your withdraw was succesfull")

  def deposit(self, amount):
    if amount > 0:
      print("Your deposit was succesfull")
      self.balance += amount
    else:
      print("Invalid amount")
  
  def check_balance(self):
    return self.balance

class SavingsAccount(Account):
  def __init__(self, balance = 0, rate = 0.5, period = 3):
    super().__init__(balance)
    self.rate = rate
    self.period = period

  def interest_calculation(self):
    interest = self.balance * self.rate * self.period
    print(f"Your interest is {interest}")

class CheckingAccount(Account):
  def __init__(self, balance = 0, overdraft = 50):
    super().__init__(balance) 
    self.overdraft = overdraft

  def withdraw(self, amount):
    if self.balance < amount - self.overdraft:
      print("You don't have enough money")
    else:
      self.balance -= amount
      print("Your withdraw was succesfull")

savings_account = SavingsAccount(balance=1000, rate=0.02, period=6)
savings_account.interest_calculation()
print(f"Balance: {savings_account.check_balance()}")
print()

checking_account = CheckingAccount(balance=500, overdraft=50)

checking_account.withdraw(600)
print(f"Balance: {checking_account.check_balance()}")
checking_account.withdraw(50)
print(f"Balance: {checking_account.check_balance()}")
checking_account.deposit(100)
print(f"Balance: {checking_account.check_balance()}")
checking_account.deposit(-50)
print(f"Balance: {checking_account.check_balance()}")