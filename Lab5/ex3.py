class Matrix:
  def __init__(self, n, m):
    self.rows = n
    self.cols = m
    self.data = [[0] * self.cols for _ in range(self.rows)]

  def get(self, row, col):
    return self.data[row][col]
  
  def set(self, row, col, value):
    self.data[row][col] = value

  def get_rows(self):
    return self.rows
  
  def get_cols(self):
    return self.cols
  
  def transpose(self):
    rows = self.get_rows()
    cols = self.get_cols()
    transp = Matrix(cols, rows)
    for row in range(rows):
      for col in range(cols):
        transp.data[col][row] = self.data[row][col]
    
    return transp
  
  def multiply(self, matrix):
    if self.get_cols() != matrix.get_rows():
      print("Cannot multiply")
      return None
    
    new_matrix = Matrix(self.get_rows(), matrix.get_cols())
    for self_row in range(self.get_rows()):
      for matrix_col in range(matrix.get_cols()):
        value = new_matrix.get(self_row, matrix_col)
        for k in range(matrix.get_rows()):
          value += self.get(self_row, k) * matrix.get(k, matrix_col)
        new_matrix.set(self_row, matrix_col, value)
    return new_matrix
  
  def transformation(self, lambda_function):
    rows = self.get_rows()
    cols = self.get_cols()
    new_matrix = Matrix(rows, cols)

    for row in range(rows):
      for col in range(cols):
        new_matrix.set(row, col, lambda_function(self.get(row, col)))
    
    return new_matrix
  
  def __str__(self):
    rows = self.get_rows()
    cols = self.get_cols()
    matrix_str = ''
    for row in range(rows):
      matrix_str += (' '.join( map(str, [self.get(row, col) for col in range(cols)])) + '\n')

    return matrix_str
  
first_matrix = Matrix(2, 3)
first_matrix.set(0, 0, 2)
first_matrix.set(0, 1, 2)
first_matrix.set(0, 2, 1)
first_matrix.set(1, 0, 3)
first_matrix.set(1, 1, 2)
first_matrix.set(1, 2, 4)

second_matrix = Matrix(3, 2)
second_matrix.set(0, 0, 1)
second_matrix.set(0, 1, 2)
second_matrix.set(1, 0, 2)
second_matrix.set(1, 1, 3)
second_matrix.set(2, 0, 4)
second_matrix.set(2, 1, 1)

print("First: ")
print(first_matrix)
print("Second: ")
print(second_matrix)

print(f"{'Get a value: '}{first_matrix.get(1, 0)} ")

print("Transpose: ")
print(first_matrix.transpose())

print("Multiplication: ")
print(first_matrix.multiply(second_matrix))

print("Tranformation with lambda: ")
print(first_matrix.transformation(lambda val: val ** 2))