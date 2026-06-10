def add(a, b):
    return a + b
def sub(a, b):
    if a>b:
	return a - b
    if b>a:
        return b - a

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
def test_sub():
    assert sub(1,2) == 1
    assert sub(-1,-2) == 1
