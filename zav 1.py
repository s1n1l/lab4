"""1. Дано рядок. Вивести окремі слова, що входять до нього, розділені пробілами, впорядкованими за
алфавітом, в стовпчик.
"""

import re


t = str(input("Введите строку : "))

out = re.sub(r'\s+', '\n', t)
print(out)