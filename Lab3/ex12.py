def group_by_rhyme(list_of_words):
  list_of_rhymes = []
  while list_of_words:
    aux = [list_of_words[0]]
    rhyme = list_of_words[0][-2:]
    list_of_words.remove(list_of_words[0])

    for x in list_of_words[:]:
      if x[-2:] == rhyme:
        aux.append(x)
        list_of_words.remove(x)
    list_of_rhymes.append(aux)
    
  return list_of_rhymes
print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))