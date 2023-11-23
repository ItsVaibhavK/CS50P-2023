import csv
import sys

argc = len(sys.argv)

# check CLA and filetype
if argc < 3:
    sys.exit("Too few command-line arguments")
elif argc > 3:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv") and not sys.argv[2].endswith(".csv"):
    sys.exit("Not a CSV file")
else:
    try:
        # empty list for each student's data as a dict
        students = []

        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            # for each row in csv
            for row in reader:
                # student is a list containing student's name split at comma as [last, first]
                student = row["name"].split(",")
                # assign first name, last name of student
                # lstrip() because of space after comma in (last, first)
                first_name = student[1].lstrip()
                last_name = student[0]
                # append each student's data as a dict to empty list
                students.append({"first": first_name, "last": last_name, "house": row["house"]})

        with open(sys.argv[2], "w") as file:
            # fieldnames are not optional for DictWriter unlike DictReader
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            # writeheader method to add fieldnames in output csv file
            writer.writeheader()
            # for each student in students list
            for student in students:
                writer.writerow({"first": student["first"], "last": student["last"], "house": student["house"]})

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")