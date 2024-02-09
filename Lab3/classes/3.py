class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


length = int(input())
width = int(input())

try:
    rectangle = Rectangle(length, width)
    print( rectangle.area())

except ValueError:
    print("Please enter valid integers for length and width.")