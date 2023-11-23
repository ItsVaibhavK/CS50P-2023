def main():
    # use convert function to get an int or raise an error
    percentage = convert(input("Fraction: ").strip())

    # print result using return str of gauge function
    print(gauge(percentage))


def convert(fraction):
    fract = fraction.split('/')
    x = fract[0]
    y = fract[1]
    if x.isdigit() and y.isdigit():
        x = abs(int(fract[0]))
        y = abs(int(fract[1]))
        if x <= y:
            # use round to round upto 2 decimal places (eg: so we get 67 instead of 66 for 2/3)
            return int(round(x / y, 2) * 100)
        elif x > y and not y == 0:
            raise ValueError
        elif y == 0:
            raise ZeroDivisionError
    # isdigit() will catch floats and non-numeric inputs
    elif not x.isdigit() or not y.isdigit():
        raise ValueError



def gauge(percentage):
    # empty
    if percentage <= 1:
        return "E"
    # full
    elif percentage >= 99:
        return "F"
    # display percentage
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()