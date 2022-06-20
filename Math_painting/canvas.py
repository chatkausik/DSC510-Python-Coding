import numpy as np
from PIL import Image


class Canvas:
    """
    Draw a canvas.
    """
    def __init__(self, width, height, color):
        self.color = color
        self.height = height
        self.width = width
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, image_path):
        img = Image.fromarray(self.data, 'RGB')
        img.save(image_path)


