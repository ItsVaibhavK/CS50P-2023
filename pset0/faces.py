# main function takes input and prints output by calling convert function
def main():
    text = input("Text: ")
    print(f"{convert(text)}")

# replace smileys by using if substring in string and replace method of string
def convert(text):
    if ":)" in text and ":(" in text:
        return text.replace(":)", "🙂").replace(":(", "🙁")
    elif ":)" in text:
        return text.replace(":)", "🙂")
    elif ":(" in text:
        return text.replace(":(", "🙁")
    else:
        return text
    
#call main
main()