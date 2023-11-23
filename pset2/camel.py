# user input
camel = input("camelCase: ").strip()
# define list to store a list of characters
temp = list(camel)

# iterate through input, use replace and str format
for i in range(len(camel)):
    if camel[i].isupper():
        temp[i] = camel[i].replace(camel[i], f"_{camel[i].lower()}")
    else:
        temp[i] = camel[i]


# snake_case output
print("snake_case: ", end="")
# print each item of list temp, use end modifier and print newline at the end outside of loop
for i in range(len(temp)):
    print(f"{temp[i]}", end="")
print()