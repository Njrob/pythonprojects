def censor(text, word):
  censored_text = text.replace(word, "*" * len(word))
  return censored_text
