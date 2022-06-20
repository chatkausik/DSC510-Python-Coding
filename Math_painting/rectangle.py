class Rectangle:
    """
    Rectangle class will take upper left co-ordinates, width and height and color.
    Some draw method which will take canvas as argument.
    """
    def __init__(self, x, y, width, height, color):
        self.color = color
        self.height = height
        self.width = width
        self.y = y
        self.x = x

    def draw_rec(self, canvas):
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color
