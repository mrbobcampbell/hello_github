class Rectangle():
    rectangles = []

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.rectangles.append((self.width, self.len))

    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l
        self.rectangles.append((self.width, self.len))

    def __repr__(self):
        return repr(self.len)


rectangle1 = Rectangle(10, 20)
rectangle2 = Rectangle(200, 200)
print(Rectangle.rectangles)
print(rectangle1.area())
rectangle1.change_size(20, 40)
print(rectangle1.area())

print(Rectangle.rectangles)
print(rectangle2.area())
print(rectangle1, "<-- this is it")
