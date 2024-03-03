import re
with open('row.txt', encoding = "utf-8") as file:
    txt = file.read()

camel_case_str = "SomeStringthatNeEDSpace"
snake_case_str = re.sub(r'([A-Z])', r'_\1', camel_case_str).lower()
print(snake_case_str)