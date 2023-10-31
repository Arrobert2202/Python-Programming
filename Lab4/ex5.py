def validate_dict(rules, dictionary):
  for key in dictionary:
    rule = None
    for r in rules:
      if key == r[0]:
        rule = r
        break
    if rule is None:
      return False
    
    rule_key, prefix, middle, suffix = rule
    value = dictionary.get(key)
    if prefix != value[0:len(prefix)] or not(len(prefix) <= value.find(middle) < len(value)-len(suffix)) or suffix != value[-len(suffix):]:
      return False
  return True

print(validate_dict([("key1", "", "inside", ""), ("key2", "start", "middle", "winter")], {"key1": "come inside, it's too cold out", "key3": "this is not valid"}))