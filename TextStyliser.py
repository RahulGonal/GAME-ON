from pyfiglet import *
from termcolor import colored
from random import randint



# fonts we are going to use
font = ['slant', "3-d", "3x5", "5lineoblique",
        "alphabet", "banner3-D", "doh", "isometric1", "letters",
        "alligator", "dotmatrix", "bubble", "bulbhead", "digital"]

# Shuffling the Font
random_choice = randint(0, len(font))

# colours we are going to use
valid_color = ('red', 'green', 'yellow', 'blue', 'cyan', 'white')
msg = input("What would you like to print ? : ")
color = input('What color do you want?: ')

if color not in valid_color:
    color = 'white'

ascii_art = figlet_format(msg, font=font[random_choice])

colored_ascii = colored(ascii_art, color)

print(colored_ascii)
