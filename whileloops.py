i = 1
while i < 6:
    print(i)
    i += 1 #ex1

i = 1
while i < 6:
  if i == 3:
    break
  i += 1 #ex2

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i) #ex3

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6") #ex4