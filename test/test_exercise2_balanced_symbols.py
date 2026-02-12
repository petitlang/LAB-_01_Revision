from exercise2_balanced_symbols import is_balanced

def test_balanced_symbols():
    assert is_balanced("({[]})") == (True, 13)
    assert is_balanced("([)]") == (False, 5)
    assert is_balanced("") == (True, 1)
    assert is_balanced("((())") == (False, 10)