def purify(num_list):
  new_list = []
  for num in num_list:
    if num % 2 == 0:
      new_list.append(num)
  return new_list
