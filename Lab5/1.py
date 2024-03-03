import re

word = "AAbbbabbbAbaabab"
print(re.findall("ab*",word))