# user input strip and lowercase
greeting = input("Greeting: ").strip().lower()

# use str method startswith()
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")