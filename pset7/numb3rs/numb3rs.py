import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        # ip = n.n.n.n where 0 <= n <= 255
        matches = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip)
        counter = 0
        # check each subgroup, converting subgroup to int, use counter to keep track
        # remember m.group(i) has to start from 1 as per lecture
        # m.group(0) seems to hold the input
        for i in range(1,5):
            if 0 <= int(matches.group(i)) <= 255:
                counter += 1
            else:
                counter = counter
        # if all 4 subgroups satisfy condition, return True
        if counter == 4:
            return True
        else:
            return False
    # if there are subgroups returning None, causing AttributeError
    except (AttributeError, ValueError):
        return False


if __name__ == "__main__":
    main()