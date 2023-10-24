def obstructed_view(heights):
  seats = []
  for row in range(len(heights)-1, 0, -1):
    for col in range(len(heights[0])):
      for i in range(row - 1, 0, -1):
        if heights[row][col] <= heights[i][col]:
          seats.append((row,col))
  return seats

heights = [[1, 2, 3, 2, 1, 1],

[2, 4, 4, 3, 7, 2],

[5, 5, 2, 5, 6, 4],

[6, 6, 7, 6, 7, 5]] 
print(obstructed_view(heights))