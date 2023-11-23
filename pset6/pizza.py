import sys
import csv
from tabulate import tabulate

# number of CLAs
argc = len(sys.argv)

# check for correct number of CLAs and correct type of file
if argc < 2:
    sys.exit("Too few command-line arguments")
elif argc > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
else:
    try:
        # empty list to populate
        table = []
        with open(sys.argv[1]) as file:
            # using reader instead of DictReader since the key names of the pizza changes
            # depending on which csv file is used
            reader = csv.reader(file)
            # append each row's data as a dict into the empty table list
            for row in reader:
                table.append({"name": row[0], "small": row[1], "large": row[2]})
        # print using tabulate with optional parameters
        print(tabulate(table, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")