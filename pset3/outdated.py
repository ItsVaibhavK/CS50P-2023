month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# infinite input loop
while True:
    try:
        date = input("Date: ").strip()
        # check if it is one of the 2 acceptable formats of mm/dd/yyyy or month-name date, year
        # code for mm/dd/yyyy format
        if "/" in date:
            date_list = date.split("/")
            m = int(date_list[0])
            d = int(date_list[1])
            y = int(date_list[2])
            if d > 31 or d < 1:
                pass
            elif m > 12 or m < 1:
                pass
            else:
                print(f"{y}-{m:02}-{d:02}")
                break
        # code for month-name date, year format
        elif "," in date:
            # first split at "," to get list of 2 items: 1. month-name date and 2. year
            date_list = date.split(",")
            # split the first item of the list into another list of 2 items: 1: month-name and 2: date
            md_date_list = date_list[0].split()
            m = md_date_list[0]
            d = int(md_date_list[1])
            y = int(date_list[1])
            if d > 31 or d < 1:
                pass
            elif m not in month:
                pass
            else:
                # get the numerical value of the month by using list.index() and adding 1 to compensate for index starting at 0
                index_month = month.index(m) + 1
                print(f"{y}-{index_month:02}-{d:02}")
                break
    except:
        pass