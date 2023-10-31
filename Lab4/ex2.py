def character_counter(string):
  counter = dict()
  for char in string:
    if char not in counter:
      counter[char] = 1
    else:
      counter[char] = counter.get(char) + 1
  return counter

print(character_counter("Ana has apples."))