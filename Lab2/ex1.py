def print_ascii_hex(first_character, n):
  ascii_hex_chars = ' '.join([format(ord(first_character) + i,"x") for i in range(n+1) ])
  print(ascii_hex_chars)

print_ascii_hex('a',25)
print_ascii_hex('A',25)
print_ascii_hex('0',9)