def nth_root(a, n):
  a = a*(10**(50*n))
  x_0 = a // 2
  for _ in range(2000):
    x_0 = (x_0 * (n - 1) // n) + (a // n) // (x_0 ** (n-1))
  result = x_0 / (10 ** 50)
  print(f"{result:.50f}")

nth_root(32,3)