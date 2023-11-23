import bank


def test_value_hello():
    assert bank.value("hello") == 0
    assert bank.value("HELLO") == 0


def test_value_h():
    assert bank.value("hey") == 20
    assert bank.value("HI") == 20


def test_default():
    assert bank.value("top of the morning to you") == 100
    assert bank.value("NAMASTE") == 100


if __name__ == "__main__":
    main()