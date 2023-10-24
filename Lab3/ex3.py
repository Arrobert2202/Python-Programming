def setOperations(a,b):
  intersection = [x for x in a if x in b]
  union = list(set(a) | set(b))
  a_minus_b = [x for x in a if x not in b]
  b_minus_a = [x for x in b if x not in a]
  return intersection, union, a_minus_b, b_minus_a
print(setOperations([1,2,3,4,5],[5,2,8,10,1]))