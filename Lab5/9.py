import re
with open('row.txt', encoding = "utf-8") as file:
    txt = file.read()

Somestring = "SomeStringthatNEEDSpace"

Spaceins_string =re.sub(r'(\w)([A-Z])',r'\1 \2', Somestring)
print(Spaceins_string)