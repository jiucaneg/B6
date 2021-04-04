class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_rectangle(self):
        return 'Rectangle (' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.width) + ', ' + str(self.height) + ')'

rect = Rectangle(5, 10, 50, 100)

print(rect.get_rectangle())
print(type(rect.get_rectangle()))