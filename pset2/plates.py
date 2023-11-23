# submitting a refined version of the problem since I discovered a bug while working on it for Unit Testing PSET5

def main():
    plate = input("Plate: ").upper().strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# if all the functions return true, is valid
def is_valid(s):
    if valid_alphanum(s):
        return True
    else:
        return False

# check if plate has alphanum characters or just alpha, check condition for both
def valid_alphanum(s):
    l = len(s)
    if valid_length(s):
        # if it only has alphabets
        if s.isalpha():
            return True
        # if it has alphabets and numbers and the first 2 characters are alphabets
        elif s.isalnum() and s[0:2].isalpha():
            # use booleans to check leading zero and numbers without following alphabets
            zero = False
            contnum = False
            # zero condition check
            for i in range(l):
                if s[i].isdigit():
                    if s[i] == "0":
                        break
                    else:
                        zero = True
                        break
            # numbers without following alphabets check
            for i in range(l):
                if (i+1) < l:
                    if s[i].isdigit() and s[i+1].isalpha():
                        break
                else:
                    contnum = True
                    break
            # if both conditions pass, return True
            if zero and contnum:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

# check if length is valid
def valid_length(s):
    l = len(s)
    if valid_characters(s):
        if 2 <= l <= 6:
            return True
        else:
            return False
    else:
        return False

# check if characters are alphanum valid
def valid_characters(s):
    if s.isalnum():
        return True
    else:
        return False


if __name__ == "__main__":
    main()