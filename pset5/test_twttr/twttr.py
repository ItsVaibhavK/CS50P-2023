def main():
    # user input, strip, call custom function
    txt = input("Input: ").strip()
    word = shorten(txt)

    # print output, loop through list, newline
    print("Output: ", end="")
    for i in range(len(word)):
        print(f"{word[i]}", end="")
    print()


def shorten(txt):
    # make a list to manipulate str
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
    # convert list to str using join (for unit testing)
    return "".join(temp)


if __name__ == "__main__":
    main()
