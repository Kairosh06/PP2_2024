def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        total_legs = 2 * num_chickens + 4 * num_rabbits
        if total_legs == numlegs:
            return num_chickens, num_rabbits
    return "No solution found"

numheads = 35
numlegs = 94
result = solve(numheads, numlegs)
if result != "No solution found":
    num_chickens, num_rabbits = result
    print(num_chickens, num_rabbits)
else :
    print("No solution")