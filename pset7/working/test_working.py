from working import convert
import pytest


# 9:00 AM to 5:00 PM
def test_format1():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("1:54 AM to 10:33 PM") == "01:54 to 22:33"
    assert convert("4:01 AM to 11:40 AM") == "04:01 to 11:40"
    assert convert("9:00 PM to 11:00 PM") == "21:00 to 23:00"
    assert convert("11:15 PM to 7:15 AM") == "23:15 to 07:15"
    assert convert("7:00 PM to 12:00 AM") == "19:00 to 00:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"


# 9 AM to 5 PM
def test_format2():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("1 AM to 10 PM") == "01:00 to 22:00"
    assert convert("4 AM to 11 AM") == "04:00 to 11:00"
    assert convert("9 PM to 11 PM") == "21:00 to 23:00"
    assert convert("11 PM to 7 AM") == "23:00 to 07:00"
    assert convert("7 PM to 12 AM") == "19:00 to 00:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test_invalid_formats():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")


if __name__ == "__main__":
    main()