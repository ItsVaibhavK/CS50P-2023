from fuel import convert, gauge
import pytest


def test_zero_div_err():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ZeroDivisionError):
        convert("100/0")
    with pytest.raises(ZeroDivisionError):
        convert("1999/0")
    with pytest.raises(ZeroDivisionError):
        convert("9999/0")


def test_value_err():
    with pytest.raises(ValueError):
        convert("x/y")
    with pytest.raises(ValueError):
        convert("!/?")
    with pytest.raises(ValueError):
        convert("one/two")
    with pytest.raises(ValueError):
        convert("4/3")


def test_valid_convert():
    assert convert("1/2") == 50
    assert convert("2/3") == 67
    assert convert("3/4") == 75
    assert convert("5/5") == 100


def test_valid_gauge():
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"


if __name__ == "__main__":
    main()