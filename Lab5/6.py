import re
with open('row.txt', encoding = "utf-8") as file:
    txt = file.read()

x = re.sub('[ ,.]', ':', txt)
print(x)