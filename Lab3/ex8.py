def ascii_codes(x=1, list=None, flag=True):
  new_list = []
  for string in list:
    char_list = []
    for char in string:
      if flag:
        if ord(char) % x == 0:
          char_list.append(char)
      else:
        if ord(char) % x != 0:
          char_list.append(char)
    new_list.append(char_list)
  return new_list
print(ascii_codes(x = 2, list = ["test", "hello", "lab002"], flag = False))