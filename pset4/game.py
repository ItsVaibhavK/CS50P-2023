# import modules
import random
import sys

# main, use loop here to keep guessing going while having a fixed value for level and the random int
def main():
    lvl = level()
    n = random.randint(1, lvl)
    while True:
        guess = guesser()
        if guess == n:
            print("Just right!")
            sys.exit()
        elif guess < n:
            print("Too small!")
            pass
        else:
            print("Too large!")
            pass

# function to get level from user and return value to main()
def level():
    while True:
        try:
            x = int(input("Level: ").strip())
            if x <= 0:
                pass
            else:
                return x
        except ValueError:
            pass

# function to get user's guess and return value to main()
def guesser():
    while True:
        try:
            x = int(input("Guess: ").strip())
            if x < 0:
                pass
            else:
                return x
        except ValueError:
            pass

# call main
main()

