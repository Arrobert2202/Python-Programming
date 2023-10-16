def nth_permutation(alphabet,p,n):
  if(n > len(alphabet)**p):
    print("n is bigger than expected")
    return
  
  permutation = ''
  for i in range(p):
    permutation += str(alphabet[n % len(alphabet)])
    n = n // len(alphabet)
  permutation = permutation[::-1]
  print(permutation)

alphabet = "ABCD"
p=3
n=40
nth_permutation(alphabet,p,n)