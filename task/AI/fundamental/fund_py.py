# 1 Определить, является ли строка палиндромом (читается одинаково слева направо и справа налево
# word_str = "radar"

def paly(s):
  st = s.lower().replace(" ", "")
  return st == st[::-1]
# print(paly(word_str))
