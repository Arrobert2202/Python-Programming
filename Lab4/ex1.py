def set_operations(a, b):
  a = set(a)
  b = set(b)

  intersection = a.intersection(b)
  union = a.union(b)
  a_minus_b = a.difference(b)
  b_minus_a = b.difference(a)
  return [intersection, union, a_minus_b, b_minus_a]

print(set_operations([1,2,5,10,32],[3,1,6,22,8,10]))