def compose(musical_notes, moves, start):
  song = []
  song.append(musical_notes[start])
  last_move = start
  for i in range(len(moves)):
    last_move += moves[i]
    last_move = last_move % len(musical_notes)
    song.append(musical_notes[last_move])
  return song
print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))