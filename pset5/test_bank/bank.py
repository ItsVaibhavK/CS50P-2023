def main():
    # user input strip and lowercase
    greeting = input("Greeting: ").strip().lower()
    print(f"${value(greeting)}")


def value(greeting):
    # use str method startswith()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()