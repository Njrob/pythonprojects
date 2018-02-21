def reverse(text):
  reversed_string = []
  text = list(text)
  for i in range(len(text) - 1, -1, -1):
    reversed_string.append(text[i])
  reversed_string = ''.join(map(str, reversed_word))
  return reversed_string
