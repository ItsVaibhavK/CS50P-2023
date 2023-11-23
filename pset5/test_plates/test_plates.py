# All vanity plates must start with at least two letters.
# Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
# Numbers cannot be used in the middle of a plate; they must come at the end. The first number used cannot be a ‘0’.
# No periods, spaces, or punctuation marks are allowed.


from plates import is_valid

def test_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False


def test_punct():
    assert is_valid("F.B.I.") == False
    assert is_valid("HE MAN") == False
    assert is_valid("A?B!C.") == False


def test_length():
    assert is_valid("CS") == True
    assert is_valid("NRVOUS") == True
    assert is_valid("OUTTATIME") == False


def test_beginning_alpha():
    assert is_valid("HE99") == True
    assert is_valid("H9") == False
    assert is_valid("99PRBM") == False


def test_alphabet():
    assert is_valid("HELLO") == True
    assert is_valid("AA") == True
    assert is_valid("JAMJAR") == True


def test_alphanum():
    assert is_valid("CS50P") == False
    assert is_valid("MV33") == True
    assert is_valid("50SC") == False


if __name__ == "__main__":
    main()