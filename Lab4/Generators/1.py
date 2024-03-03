#Create a generator that generates the squares of numbers up to some number N.

def squares_generator(N):
    for i in range(N):
        yield i ** 2

n = int(input())
square = squares_generator(n)
for square in squares:
    print(shit)   