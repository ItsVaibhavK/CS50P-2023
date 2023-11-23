import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    # try block
    try:
        # 12 hr input, 24 hr output
        # format 1           (1-12):(00-59)  (AM or PM)  (1-12):(00-59)  (AM or PM)
        if matches:= re.fullmatch(r"(\d+):(\d+) (AM|PM) to (\d+):(\d+) (AM|PM)", s):
            hour1 = int(matches.group(1))
            minute1 = int(matches.group(2))
            hour2 = int(matches.group(4))
            minute2 = int(matches.group(5))
            # valid time range
            if 1 <= hour1 <= 12 and 1 <= hour2 <= 12 and 0 <= minute1 <= 59 and 0 <= minute2 <= 59:
                # time 1
                if matches.group(3) == "AM":
                    if hour1 < 10:
                        time1 = (f"0{matches.group(1)}:{matches.group(2)}")
                    elif 10 <= hour1 < 12:
                        time1 = (f"{matches.group(1)}:{matches.group(2)}")
                    else:
                        time1 = (f"00:{matches.group(2)}")
                elif matches.group(3) == "PM":
                    if hour1 < 12:
                        time1 = (f"{hour1 + 12}:{matches.group(2)}")
                    else:
                        time1 = (f"{matches.group(1)}:{matches.group(2)}")
                # time 2
                if matches.group(6) == "AM":
                    if hour2 < 10:
                        time2 = (f"0{matches.group(4)}:{matches.group(5)}")
                    elif 10 <= hour2 < 12:
                        time2 = (f"{matches.group(4)}:{matches.group(5)}")
                    else:
                        time2 = (f"00:{matches.group(5)}")
                elif matches.group(6) == "PM":
                    if hour2 < 12:
                        time2 = (f"{hour2 + 12}:{matches.group(5)}")
                    else:
                        time2 = (f"{matches.group(4)}:{matches.group(5)}")
                # output
                return (f"{time1} to {time2}")
            # invalid time range
            else:
                raise ValueError
        # format 2                 (1-12) (AM or PM)    (1-12) (AM or PM)
        elif matches:= re.fullmatch(r"(\d+) (AM|PM) to (\d+) (AM|PM)", s):
            hour1 = int(matches.group(1))
            hour2 = int(matches.group(3))
            # valid time range
            if 1 <= hour1 <= 12 and 1 <= hour2 <= 12:
                # time 1
                if matches.group(2) == "AM":
                    if 1 <= hour1 < 10:
                        time1 = (f"0{matches.group(1)}:00")
                    elif 10 <= hour1 < 12:
                        time1 = (f"{matches.group(1)}:00")
                    else:
                        time1 = ("00:00")
                elif matches.group(2) == "PM":
                    if hour1 < 12:
                        time1 = (f"{hour1 + 12}:00")
                    else:
                        time1 = (f"{matches.group(1)}:00")
                # time 2
                if matches.group(4) == "AM":
                    if 1 <= hour2  < 10:
                        time2 = (f"0{matches.group(3)}:00")
                    elif 10 <= hour2 < 12:
                        time2 = (f"{matches.group(3)}:00")
                    else:
                        time2 = ("00:00")
                elif matches.group(4) == "PM":
                    if hour2 < 12:
                        time2 = (f"{hour2 + 12}:00")
                    else:
                        time2 = (f"{matches.group(3)}:00")
                # output
                return (f"{time1} to {time2}")
            # invalid time range
            else:
                raise ValueError
        # invalid input
        else:
            raise ValueError
    # except block
    except (AttributeError, ValueError):
        raise


if __name__ == "__main__":
    main()