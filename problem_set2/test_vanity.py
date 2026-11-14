from vanity import is_valid

def test_is_valid():
    assert is_valid("CS50") == "Valid"
    assert is_valid("cS50") == "Valid"
    assert is_valid("cs50") == "Valid"