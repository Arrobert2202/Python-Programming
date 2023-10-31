def operations_dict(*sets):
  new_dict = dict()
  for i in range(len(sets) - 1):
    for j in range(i+1, len(sets)):
      key_string = f"{sets[i]} | {sets[j]}"
      new_dict[key_string] = sets[i].union(sets[j])

      key_string = f"{sets[i]} & {sets[j]}"
      new_dict[key_string] = sets[i].intersection(sets[j])

      key_string = f"{sets[i]} - {sets[j]}"
      new_dict[key_string] = sets[i].difference(sets[j])

      key_string = f"{sets[j]} - {sets[i]}"
      new_dict[key_string] = sets[i].difference(sets[j])
  return new_dict
dictionary = operations_dict(set([1,2]),set([2,3]))
for key, value in dictionary.items():
  print(f"{key} : {value}")