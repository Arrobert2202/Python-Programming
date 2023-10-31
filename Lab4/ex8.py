def loop(mapping):
  visited = ['start']
  key = mapping.get('start')

  while key not in visited:
    visited.append(key)
    key = mapping.get(key)
  return visited[1:]
print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))