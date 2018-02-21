def anti_vowel(text):
  text = text.translate(None, "aeiouAEIOU")
  return text
