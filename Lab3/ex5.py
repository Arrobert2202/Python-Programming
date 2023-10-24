def zero_below_diagonal(matrix):
  for row in range(len(matrix)):
    for col in range(len(matrix[0])):
      if col < row:
        matrix[row][col] = 0
  return matrix
matrix = zero_below_diagonal([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
for row in matrix:
  print(row)