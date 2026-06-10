def add(a, b):
    return a + b

def sub(a, b):
    return abs(a - b)

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0

def test_sub():
    assert sub(1, 2) == 1
    assert sub(-1, -2) == 1
