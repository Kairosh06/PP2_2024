import re
word = "RRR_gkh_qwe"
"""with open('row.txt', encoding = "utf-8") as file:
    txt = file.read()"""
x = re.findall(r'[a-z] + _[a-z]+', word)
print(x)