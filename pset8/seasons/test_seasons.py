from seasons import user_dob
import pytest, datetime

def test_valid_input():
    assert user_dob("2019-12-04") == datetime.date(2019, 12, 4)
    assert user_dob("1992-09-17") == datetime.date(1992, 9, 17)
    assert user_dob("1965-08-25") == datetime.date(1965, 8, 25)
    assert user_dob("1963-12-19") == datetime.date(1963, 12, 19)
    assert user_dob("1991-10-04") == datetime.date(1991, 10, 4)

def test_invalid_input():
    with pytest.raises(SystemExit):
        user_dob("December 21st, 1969")
    with pytest.raises(SystemExit):
        user_dob("February 21")
    with pytest.raises(SystemExit):
        user_dob("02-12-1955")
    with pytest.raises(SystemExit):
        user_dob("October")
    with pytest.raises(SystemExit):
        user_dob("45-30-0000")
