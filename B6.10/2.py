class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def rectangle_area(self):
        return self.width * self.length

rectangle = Rectangle(10, 20)

print(rectangle.rectangle_area())