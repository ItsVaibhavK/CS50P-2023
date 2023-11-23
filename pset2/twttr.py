# user input, strip, make a list to manipulate str
txt = input("Input: ").strip()
temp = list(txt)

# use for loop, splice and match syntax to replace vowels specifically
for i in range(len(txt)):
    match txt[i]:
        case "a" | "A":
            temp[i] = ""
        case "e" | "E":
            temp[i] = ""
        case "i" | "I":
            temp[i] = ""
        case "o" | "O":
            temp[i] = ""
        case "u" | "U":
            temp[i] = ""
        case _:
            temp[i] = txt[i]

# print output, loop through list, newline
print("Output: ", end="")
for i in range(len(temp)):
    print(f"{temp[i]}", end="")
print()
