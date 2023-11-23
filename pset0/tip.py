def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # use replace method of string and use float(str) to convert str to float
    return float(d.replace("$", ""))


def percent_to_float(p):
    # use replace method of string and use float(str) to convert str to float and divide by 100 as per instructions in pset
    return float(p.replace("%", "")) / 100


main()