from colorama import init
from os import get_terminal_size, system
from PIL.Image import open as open_im
from time import sleep


im = open_im(input())
im = im.convert("RGB")
w, h = im.size
tw, th = get_terminal_size()

if ((w * 2) > tw) | (h > th):
    w2 = round(tw / 2) - 2
    h2 = round(h * (w2 / w))

print(w2, h2)

im = im.resize((w2, h2))

init()



def color(r, g, b):
    return f"\033[38;2;{r};{g};{b}m██\033[0m"

for i in range(h2):
    for j in range(w2):
        print(color(*im.getpixel((j, i))), end="")
    print()
    sleep(1 / 24)

exit(system("PAUSE"))
