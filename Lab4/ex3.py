def compare_operation(dict1, dict2):
  if list(dict1.keys()) != list(dict2.keys()):
    return False
  
  for key in dict1.keys():
    if ((type(dict1[key]) is dict) and (type(dict2[key]) is dict)) or ((type(dict1[key]) is set) and (type(dict2[key]) is set)) or (type(dict1[key]) is list) and (type(dict2[key]) is list):
      if not compare_operation(dict1[key], dict2[key]):
        return False
    elif dict1[key] != dict2[key]:
      return False
  return True
print(compare_operation({'a': 1, 'b': 3, 'c': {'d' : 5}}, {'a': 1, 'b': 3, 'c': {'d' : 7}}))
