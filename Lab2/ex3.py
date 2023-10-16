def impartire_cu_virgula(numarator, numitor):
  result = str(numarator // numitor) + ','
  rest = numarator % numitor
  for _ in range(100):
    rest *= 10
    decimal = str(rest // numitor)
    rest = rest % numitor 
    result += decimal
  print(result)

impartire_cu_virgula(12, 11)