import re
word = "aanythinsdf12b"
x = re.findall('a.*b$', word)
print(x)