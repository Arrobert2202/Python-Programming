def count_matches(*pos_args,**key_args):
  counter = 0
  args_values = key_args.values()
  for arg in pos_args:
    if arg in args_values:
      counter += 1
  return counter
print(count_matches(1, 2, 3, 4, x=1, y=2, z=3, w=5))