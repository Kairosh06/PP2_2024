fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) #ex1

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) #ex2

for x in range(6):
  print(x) #ex3

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) #ex4