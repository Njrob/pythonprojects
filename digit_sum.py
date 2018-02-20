def digit_sum(x):
  x = str(x)
  total = 0
  for n in range(len(x)):
    total += int(x[n])
  return total
