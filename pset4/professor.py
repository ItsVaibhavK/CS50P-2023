import random
import sys


def main():
    level = get_level()
    score = 0
    # generate 10 problems
    for i in range(10):
        error_counter = 0
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y
        # use infinite loop for answers, use error_counter to keep track of incorrect attempts
        # break loop if correct answer, print EEE if incorrect answer
        # if 3 incorrect attempts, display solution and break loop
        while True:
            answer = input(f"{x} + {y} = ").strip()
            if int(answer) == z:
                score += 1
                break
            elif int(answer) != z or not answer.isnumeric():
                error_counter += 1
                print("EEE")
            if error_counter == 3:
                print(f"{x} + {y} = {z}")
                break

    # output score
    print(f"Score: {score}")


def get_level():
    # infinite loop to get level 1, 2, 3
    # use return to break loop
    while True:
        try:
            level = int(input("Level: ").strip())
            if not 0 < level < 4:
                pass
            else:
                return level
        except ValueError:
            pass


def generate_integer(level):
    # generate random integer based on level
    try:
        if level == 1:
            return random.randint(0, 9)
        elif level == 2:
            return random.randint(10, 99)
        elif level == 3:
            return random.randint(100, 999)
        else:
            raise ValueError
    except ValueError:
        sys.exit("Incorrect usage.")













if __name__ == "__main__":
    main()