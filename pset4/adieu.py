# import relevant module
import inflect

p = inflect.engine()

# initialize empty list
names = []

# infinite loop for user input
while True:
    try:
        name = input("Name: ").strip()
        # add name to list, avoid duplicating names
        if name not in names:
            names.append(name)
        else:
            pass
    # break out of loop, remember newline to move cursor
    except EOFError:
        print()
        break

# store formatted list of names
names_f = p.join(names)
# output, baby
print("Adieu, adieu, to", names_f)
