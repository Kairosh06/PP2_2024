"""Define a function with a generator which can iterate the numbers, 
which are divisible by 3 and 4, between a given range 0 and n."""

def divisibles(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
for num in divisibles(n):
    print(num)