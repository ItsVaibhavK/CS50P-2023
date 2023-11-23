def main():
    # call function
    z = fuel()
    # empty
    if z <= 1:
        print("E")
    # full
    elif z >= 99:
        print("F")
    # display percentage
    else:
        print(f"{z}%")

def fuel():
    # infinite loop for correct input
    while True:
        try:
            fract = input("Fraction: ").strip().split('/')
            x = abs(int(fract[0]))
            y = abs(int(fract[1]))
            if x <= y:
                # use round to round upto 2 decimal places (eg: so we get 67 instead of 66 for 2/3)
                return int(round(x / y, 2) * 100)
        except (ValueError, ZeroDivisionError):
            pass

main()
