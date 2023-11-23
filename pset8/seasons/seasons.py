import sys, inflect
from datetime import date, timedelta

p = inflect.engine()


def main():
    total_minutes = delta(user_dob(input("Date of birth: ")))
    # output result using inflect
    print((f"{p.number_to_words(total_minutes, andword='')} minutes").capitalize())


# return user dob in correct format or exit
def user_dob(dob):
    try:
        return date.fromisoformat(dob)
    except ValueError:
        sys.exit("Invalid format")


# return total number of minutes passed
def delta(dob):
    difference = date.today() - dob
    # get difference as total seconds, divide by 60 to get total minutes
    return int(timedelta.total_seconds(difference) / 60)


if __name__ == "__main__":
    main()
