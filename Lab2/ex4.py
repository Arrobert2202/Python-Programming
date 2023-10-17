def system_solver(A, B):
  if len(A) != len(A[0]) or len(A) != len(B):
    print("Dimensions not equal")
    return
  
  
A = [[4, 3, 3, -3],
     [1, 3, 5, 8],
     [5, 6, 8, 0],
     [-10, 4, 3, 7]]

B = [4, 10, -20, 5]
system_solver(A, B)