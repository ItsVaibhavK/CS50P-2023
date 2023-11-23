def main():
    # user input
    time = input("What time is it? ").strip().lower()

    # 12 hour input with a.m. or p.m. // .split() ran into errors earlier when 24h format was input
    if time.endswith("a.m.") or time.endswith("p.m."):
        t12hf(time)
    # 24 hour input
    else:
        t24hf(time)

def convert(time):
    # split input text and assign to variables
    hours, minutes = time.split(":")
    # convert str to float
    h = float(hours)
    m = float(minutes)
    # calculate time based on hours and return
    return h + m / 60

def t12hf(time):
        timenum, timesuffix = time.split()
        # call function on only numerical part of input
        t = convert(timenum)
        # 12 hour output a.m.
        if timesuffix == "a.m." and 7.0 <= t <= 8.0:
            print("breakfast time")
        # 12 hour output p.m.
        elif timesuffix == "p.m.":
            if 12.0 <= t <= 12.99 or t == 1.0:
                print("lunch time")
            elif 6.0 <= t <= 7.0:
                print("dinner time")

def t24hf(time):
        # call function on input as it does not have non-numerical parts
        t = convert(time)
        # output based on condition
        if 7.0 <= t <= 8.0:
            print("breakfast time")
        elif 12.0 <= t <= 13.0:
            print("lunch time")
        elif 18.0 <= t <= 19.0:
            print("dinner time")

if __name__ == "__main__":
    main()