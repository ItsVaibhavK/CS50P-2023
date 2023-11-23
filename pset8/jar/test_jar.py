import pytest
from jar import Jar


# testing initializing objects of type jar, capacity as defined in parenthesis
# default capacity is 12 (see last line Jar())
def test_init():
    jar = Jar(4)
    assert jar.capacity == 4
    with pytest.raises(ValueError):
        jar = Jar(-9)
    jar = Jar(7)
    assert jar.capacity == 7
    jar = Jar()
    assert jar.capacity == 12


# testing str output of cookies
def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(2)
    assert str(jar) == "🍪🍪"
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(4)
    assert str(jar) == "🍪🍪🍪"
    jar.withdraw(2)
    assert str(jar) == "🍪"


# testing deposit method
def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)
    with pytest.raises(ValueError):
        jar.deposit(90)
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(7)
    assert jar.size == 12


# testing withdraw method
def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(15)
    with pytest.raises(ValueError):
        jar.withdraw(60)
    jar.deposit(12)
    jar.withdraw(7)
    assert jar.size == 5
    jar.withdraw(4)
    assert jar.size == 1
