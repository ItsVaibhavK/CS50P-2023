from numb3rs import validate

def test_range():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("300.25.204.1") == False
    assert validate("999.888.777.666") == False
    assert validate("23.999.555.444") == False


def test_structure():
    assert validate("cat") == False
    assert validate("23.24.25.22.") == False
    assert validate("1.2.3") == False
    assert validate("1") == False
    assert validate("245/3?123!24") == False
    assert validate("a.b.c.d") == False
    assert validate("1.2.3.4") == True


if __name__ == "__main__":
    main()