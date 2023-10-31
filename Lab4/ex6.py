def unique_duplicate(numbers_list):
  unique_numbers = set(numbers_list)
  return (len(unique_numbers), len(numbers_list) - len(unique_numbers))
print(unique_duplicate([1, 2, 3, 4, 5, 2, 6, 7, 5, 6, 10]))