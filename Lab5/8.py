import re
"""with open('row.txt', encoding = "utf-8") as file:
    txt = file.read()"""
Uppercase_string = "HelloWorld"
split_string = re.findall('[A-Z][^A-Z]*', Uppercase_string)
print(split_string)