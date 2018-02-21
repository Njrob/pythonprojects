def remove_duplicates(int_list):
  new_list = []
  for i in int_list:
    if i not in new_list:
      new_list.append(i)
  return new_list
