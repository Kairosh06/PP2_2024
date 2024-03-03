import re
word = "abbbAbbab"
"""with open('row.txt', encoding = "utf-8") as file:
    txt = file.read()"""

x = re.findall(r'a.*?b{2,3}', word)

print(x)