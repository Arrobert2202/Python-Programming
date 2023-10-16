def bits_sequence(numbers):
  sequence = ' '
  for number in numbers:
    sequence += '{:08b}'.format(number) + ' '
  sequence = sequence.rstrip()
  print(sequence, sequence.count('0'), sequence.count('1'))
numbers = [0, 1, 2, 3, 4]
bits_sequence(numbers)