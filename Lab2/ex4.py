def system_solver(A, B):
  if len(A) != len(A[0]) or len(A) != len(B):
    print("Dimensions not equal")
    return
  
  
A = [[2, 1, -1, 3],
     [1, 3, 2, 7],
     [3, 2, 4, 10],
     [4, 0, 3, 8]]

B = [4, 10, 15, 12]
system_solver(A, B)