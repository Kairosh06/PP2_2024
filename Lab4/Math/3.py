import math

def area_of_polygon(n, s):
    return (n * s**2) / (4 * math.tan(math.pi / n))

n = int(input())
s = float(input())

area = area_of_polygon(n, s)

print(area)