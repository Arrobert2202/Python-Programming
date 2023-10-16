def nth_root(a, n):
  a = a*(10**(50*n))
  x_0 = a // 2
  for _ in range(2000):
    x_0 = (x_0 * (n - 1) // n) + (a // n) // (x_0 ** (n-1))
  print(x_0 / (10 ** 50))

nth_root(20,4)