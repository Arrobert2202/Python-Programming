def is_palindrome(number):
  return str(number) == str(number)[::-1]

def tuple_palindromes(numbers):
  palindromes = []
  for number in numbers:
    if is_palindrome(number):
      palindromes.append(number)
  palindromes.sort()
  return(len(palindromes), palindromes[-1]) 

print(tuple_palindromes([22,323,41,532,8228,3424]))