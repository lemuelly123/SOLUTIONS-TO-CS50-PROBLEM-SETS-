from vanity import is_valid

def test_is_valid_true():
    assert is_valid("CS50") == True
    assert is_valid("cS50") == True
    assert is_valid("cs50") == True

def test_is_valid_false():
    assert is_valid("CS05") == False
    assert is_valid("AAA") == False