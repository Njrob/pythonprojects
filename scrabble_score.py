def scrabble_score(word):
  total_score = 0
  word = word.lower()
  for char in range(len(word)):
    for value in score:
      if value == word[char]:
        total_score += score[value]
  return total_score
