
class Square:
    """
    Square class will take upper left co-ordinates, side and color.
    Some draw method which will take canvas as argument.
    """
    def __init__(self, x, y, side, color):
        self.color = color
        self.side = side
        self.y = y
        self.x = x

    def draw_sqr(self, canvas):
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color

