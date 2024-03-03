import re
"""with open('row.txt', encoding = "utf-8") as file:
    txt = file.read()"""

snake_case_str = "_some_snake_case_string"
camel_case_str = snake_case_str.split('_')[0] + ''.join(word.title() for word in snake_case_str.split('_')[1:])
print(camel_case_str)