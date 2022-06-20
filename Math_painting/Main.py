import numpy as np
from PIL import Image
from canvas import Canvas
from square import Square
from rectangle import Rectangle

canvas_width = int(input("Enter the width of your canvas: "))
canvas_height = int(input("Enter the height of your canvas: "))

colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter the color fo your canvas(black/white): ")

canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
    shape_type = input("What shape do you want to draw(square/rectangle), or type quit to exit: ")
    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter x co-ordinates: "))
        rec_y = int(input("Enter y co-ordinates: "))
        rec_height = int(input("Enter rectangle height: "))
        rec_width = int(input("Enter rectangle width: "))
        red = int(input("How much red do you want in your rectangle: "))
        green = int(input("How much green do you want in your rectangle: "))
        blue = int(input("How much blue do you want in your rectangle: "))
        rec = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red, green, blue))
        rec.draw_rec(canvas)
    elif shape_type.lower() == "square":
        sqr_x = int(input("Enter x co-ordinates: "))
        sqr_y = int(input("Enter y co-ordinates: "))
        sqr_side = int(input("Enter square side: "))
        red = int(input("How much red do you want in your square: "))
        green = int(input("How much green do you want in your square: "))
        blue = int(input("How much blue do you want in your square: "))
        sqr = Square(x=sqr_x, y=sqr_y, side=sqr_side, color=(red, green, blue))
        sqr.draw_sqr(canvas)
    else:
        canvas.make("canvas.png")
        break


