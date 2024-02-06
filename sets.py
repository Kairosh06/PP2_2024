fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!") #ex1

fruits = {"apple", "banana", "cherry"}
fruits.add("orange") #ex2

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits) #ex3

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana") #ex4

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana") #ex5 