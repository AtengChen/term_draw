from PIL.Image import *
from os import system


file = input()
im = open(file)

w = im.width
h = im.height

new_im = new("L", (w, h))

for y in range(h):
    for x in range(w):
        try:
            if im.getpixel((x, y)) != im.getpixel((x + 1, y)):
                new_im.putpixel((x, y), 255)
            else:
                new_im.putpixel((x, y), 0)
        except:
            pass

new_im.save("hello2.png", "png")

def get_p(x, y, f=new_im):
    try:
        state = (f.getpixel((x - 1, y + 1)), f.getpixel((x, y + 1)), f.getpixel((x + 1, y + 1)),
                f.getpixel((x - 1, y)),     f.getpixel((x, y)),     f.getpixel((x + 1, y))    ,
                f.getpixel((x - 1, y - 1)), f.getpixel((x, y - 1)), f.getpixel((x + 1, y - 1)))
    except:
        state = (0, 0, 0,
                 0, 0, 0,
                 0, 0, 0)

    d = {(0, 255, 0,
          0, 255, 0,
          0, 255, 0): "│",

         (0, 0, 0,
          255, 255, 255, 
          0, 0, 0): "─",
         
         (0, 0, 0,
          0, 255, 255,
          0, 255, 0): "┌",
         
         (0, 0, 0,
          255, 255, 0,
          0, 255, 0): "┐",
         
         (0, 255, 0,
          0, 255, 255,
          0, 0, 0): "└",
         
         (0, 255, 0,
          255, 255, 0,
          0, 0, 0): "┘",
         
         (0, 255, 0,
          0, 255, 255,
          0, 255, 0): "├",
         
         (0, 0, 0,
          255, 255, 255,
          0, 255, 0): "┬",
         
         (0, 255, 0,
          255, 255, 255,
          0, 0, 0): "┴",
         
         (0, 255, 0,
          255, 255, 0,
          0, 255, 0): "┤",
         
         (255, 0, 0,
          0, 255, 0,
          0, 0, 255): "╲",
         
         (0, 0, 255,
          0, 255, 0,
          255, 0, 0): "╱",
         
         (255, 0, 255,
          0, 255, 0,
          255, 0, 255): "╳",
         
         (255, 255, 255,
          255, 255, 255,
          255, 255, 255): "█",
         
         (0, 0, 0,
          0, 0, 0,
          0, 0, 0): " "
         }

    try:
        return d[state]
    except KeyError:
        return " "


s = ""
for i in range(1, h - 1, 3):
    for j in range(1, w - 1, 3):
        s += get_p(j, i)
    s += "\n"


print(s)
system("pause")