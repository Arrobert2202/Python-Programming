def is_prime(x):
  if x <= 1:
    return False
  elif x <= 3:
    return True
  if x % 2 == 0:
    return False
  for i in range(3, int(x ** 0.5) + 1, 2):
    if x % i == 0:
      return False
  return True

def primeList(numbers):
  prime_integers = [x for x in numbers if is_prime(x)]
  return prime_integers

print(primeList([2,4,5,11,14,35,101]))