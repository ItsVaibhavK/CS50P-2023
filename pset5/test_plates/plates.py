# All vanity plates must start with at least two letters.
# Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
# Numbers cannot be used in the middle of a plate; they must come at the end. The first number used cannot be a ‘0’.
# No periods, spaces, or punctuation marks are allowed.

def main():
    plate = input("Plate: ").upper().strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


# if all the functions return true, is valid
# restructured multiple functions into 1 function for PSET5 Unit Testing
def is_valid(s):
    # if valid characters
    if s.isalnum() or s.isalpha():
        l = len(s)
        # if valid length
        if 2 <= l <= 6:
            # if it only has alphabets
            if s.isalpha():
                return True
            # if it has alphabets and numbers and the first 2 characters are alphabets
            elif s.isalnum() and s[0:2].isalpha():
                # use booleans to check leading zero and numbers without adjacent alphabets
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
                # numbers without adjacent alphabets check
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
    else:
        return False


if __name__ == "__main__":
    main()