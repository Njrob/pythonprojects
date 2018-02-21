def median(int_list):
  int_list = sorted(int_list)
  if len(int_list) % 2 == 0:
    med = float((int_list[((len(int_list) / 2) - 1)] + int_list[((len(int_list) / 2))])) / 2
  else:
    med = (int_list[(len(int_list) - 1) / 2])
  return med
