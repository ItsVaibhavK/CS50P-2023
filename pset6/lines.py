# to use sys.exit
import sys

def main():
    # number of CLAs
    argc = len(sys.argv)

    # check for correct number of CLAs, and if sys.argv[1] is a python file
    if argc < 2:
        sys.exit("Too few command-line arguments")
    elif argc > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        # try-except block to open the file in read-mode, count and print the number of lines
        try:
            counter = 0
            with open(sys.argv[1], "r") as file:
                for line in file:
                    if line_counter(line):
                        counter += 1
            print(f"{counter}")
        except FileNotFoundError:
            sys.exit("File does not exist")


def line_counter(line):
    # don't count lines that are comments, blank lines (count docstrings though)
    # lstrip() to remove indent and then check if it is a comment
    if not line.lstrip().startswith("#") and not line.isspace():
        return True
    else:
        return False


if __name__ == "__main__":
    main()