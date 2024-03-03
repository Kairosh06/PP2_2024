import math

def degree_to_radian(degree):
    return math.radians(degree)

degree = float(input())
radian = degree_to_radian(degree)

print(radian)