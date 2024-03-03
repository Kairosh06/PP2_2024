import re
word = "RRRasdFFg"
"""with open('row.txt', encoding = "utf-8") as file:
    txt = file.read()"""

x = re.findall(r'[A-Z][a-z]+', word)
print(x)