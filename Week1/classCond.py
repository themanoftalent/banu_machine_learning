class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


# point1 = Point()
# point1.x = 10
# point1.y = 19

# here we display our objects
# print(point1.x)
# print(point1.y)
# point1.draw()
# point1.move()

point2 = Point(10, 20)
point2.y = 45
print(point2.x, point2.y)
