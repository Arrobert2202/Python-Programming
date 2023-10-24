def fibonacci(n):
  fibo = []
  if n >= 0:
    fibo.append(0)
  if n > 0:
    fibo.append(1)
  while len(fibo) <= n:
    value = fibo[len(fibo) - 1] + fibo[len(fibo) - 2]
    fibo.append(value)
  return fibo

print(fibonacci(15))