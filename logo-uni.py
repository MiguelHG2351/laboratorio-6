import os


COLORS = {
    "black": "\u001b[30;1m",
    "red": "\u001b[31;1m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33;1m",
    "blue": "\u001b[34;1m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "yellow-background": "\u001b[43m",
    "black-background": "\u001b[40m",
    "cyan-background": "\u001b[46;1m",
}


def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text


f = open('./logo.txt', "r")

ascii = "".join(f.readlines())

print("\033[0;37;48m \033[0;37;48m")  # Regresa los colores a la normalidad
print(colorText(ascii))
print("\033[0;37;48m \033[0;37;48m")  # Regresa los colores a la normalidad
