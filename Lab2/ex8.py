def calculate_area(y):
  sum1 = 0
  sum2 = 0
  for i in range(len(y)-1):
    sum1 += i * y[i+1]
    sum2 += (i+1) * y[i]
  sum2 += y[len(y)-1] * (len(y)-1)
  print(sum1)
  print(sum2)
  area = abs(sum1-sum2)/2
  print(area)

y = [6,6,6,6,7,8,9,9,9,8,12,14,13,9,8,8,8,4,3,3,3]
calculate_area(y)