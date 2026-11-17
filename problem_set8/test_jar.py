import pytest
from jar import Jar


def test_valid_jar_capacity():
    jar1 = Jar()
    jar2 = Jar(10)
    assert jar1.capacity == 12
    assert jar2.capacity == 10


def test_invalid_jar_capacity():
    jar1 = Jar()
    jar2 = Jar(10)
    with pytest.raises(ValueError):
        assert Jar(-1)
        assert Jar(0)
        assert jar1.capacity == 0.5
        assert jar1.capacity == -1.3

def test_valid_deposit():
    jar1 = Jar()
    jar2 = Jar(10)
    assert jar1.deposit(12)
    assert jar2.deposit(1)

def test_invalid_deposit():
    jar1 = Jar()
    jar2 = Jar(10)
    with pytest.raises(ValueError):
        assert jar1.deposit(13)
        assert jar2.deposit(11)
        assert jar1.deposit(-1)
        assert jar2.deposit(0)
        assert jar1.deposit(1.4)

def test_valid_withdraw():
    jar1 = Jar()
    jar2 = Jar(10)
    jar1.deposit(10)
    jar2.deposit(10)
    withdraw1 = jar1.withdraw(1)
    withdraw2 = jar2.withdraw(7)
    assert withdraw1 == 9
    assert withdraw2 == 3

def test_invalid_withdraw():
    jar1 = Jar()
    jar2 = Jar(10)
    jar1.deposit(10)
    jar2.deposit(9)
    with pytest.raises(ValueError):
        assert jar1.withdraw(11)
        assert jar2.withdraw(10)
        assert jar1.withdraw("")
        assert jar2.withdraw("")

def test_jar_size():
    jar1 = Jar()
    jar2 = Jar(10)
    jar3 = Jar()
    jar1.deposit(3)
    jar2.deposit(2)
    assert jar1.size == 3
    assert jar2.size == 2
    assert jar3.size == 0


def test_str_jar():
    jar1 = Jar()
    jar2 = Jar(10)
    jar3 = Jar()
    jar1.deposit(3)
    jar2.deposit(2)
    assert str(jar1) == "Number of cookies are: 🍪🍪🍪"
    assert str(jar2) == "Number of cookies are: 🍪🍪"
    assert str(jar3) == "Empty cookie jar"