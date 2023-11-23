import re
import sys


def main():
    print(count(input("Text: ").strip()))


def count(s):
    # findall returns a list or tuple of matches
    # len of list == number of matches
    # r'\bfoo\b' matches 'foo', 'foo.', '(foo)', 'bar foo baz' but not 'foobar' or 'foo3'
    return len(re.findall(r"\b(um)\b", s, re.IGNORECASE))


if __name__ == "__main__":
    main()