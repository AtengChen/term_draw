from colorama import init
from os import get_terminal_size, system
from PIL.Image import open as open_im
from time import sleep


im = open_im(input("File: "))
shade_flag = bool(input("Shade? [<blank>(No) / <no-blank>(Yes)] "))
alg_num = int(input("Alg: "))

im = im.convert("RGB")
w, h = im.size
tw, th = get_terminal_size()

if ((w * 2) > tw) | (h > th):
    w2 = round(tw / 2) - 2
    h2 = round(h * (w2 / w))

print(w2, h2)

im = im.resize((w2, h2))

init()



def color(r, g, b, shade=False, alg_num=3):
    if shade:
        char = [" ", "░", "▒", "▓", "█"]
    else:
        char = ["█"]
    algs = [lambda: (r + g + b) / 3,
            lambda: 0.2126 * r + 0.7152 * g + 0.0722 * b,
            lambda: max(r, g, b),
            lambda: min(r, g, b)]
    a = 255 - algs[alg_num]()
    return f"\033[38;2;{r};{g};{b}m{char[round(a / 255 * len(char)) - 1] * 2}\033[0m"

for i in range(h2):
    for j in range(w2):
        print(color(*im.getpixel((j, i)), shade=shade_flag, alg_num=alg_num), end="")
    print()
    sleep(1 / 24)

exit(system("PAUSE"))
