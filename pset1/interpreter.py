# user input, split and each element assigned to a separate variable immediately
x, y, z = input("Expression: ").split()

# convert str to float
x = float(x)
z = float(z)

match y:
    case "+":
        print(f"{x + z}")
    case "-":
        print(f"{x - z}")
    case "*":
        print(f"{x * z}")
    case "/":
        print(f"{x / z}")
    case _:
        print("Invalid operator.")