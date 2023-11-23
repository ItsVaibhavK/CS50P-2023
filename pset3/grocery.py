# declare empty dict outside and not in the loop, you fool
glist = {}

# infinite loop for input
while True:
    try:
        item = input().strip().upper()
        # if the key exists add 1 to value pair
        if item in glist:
            glist[item] += 1
        # if the key doesn't exist, add the key to dict and add 1 as value pair
        else:
            glist[item] = 1
    except EOFError:
        print()
        break

# output using sorted() and .keys() to iterate over list of keys and sort alphabetically
for x in sorted(glist.keys()):
    # print value, key
    print(glist[x], x)