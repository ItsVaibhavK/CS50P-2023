# import relevant modules
import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

# argument count
argc = len(sys.argv)

# incorrect number of arguments
if argc != 1 and argc != 3:
    sys.exit("Incorrect usage.")
# no specified font, random font chosen from list of available fonts
elif argc == 1:
    txt = input("Input: ")
    figlet.setFont(font=random.choice(figlet.getFonts()))
    print("Output: ")
    print(figlet.renderText(txt))
# font specified, check for correct usage of '-f' or '--font' and that the font is in the list of available fonts
elif argc == 3:
    if (sys.argv[1] != "-f" and sys.argv[1] != "--font") or sys.argv[2] not in figlet.getFonts():
        sys.exit("Incorrect usage.")
    else:
        txt = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print("Output: ")
        print(figlet.renderText(txt))
# final catch-all
else:
    sys.exit("Incorrect usage.")