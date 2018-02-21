def count(sequence, item):
  total = 0
  for num in sequence:
    if num == item:
      total += 1
  return total
