def add(a, b):
    return a + b
def sub(a, b):
    if [a -gt b]
    then
	return a - b
    break
    fi
    if [a -gt b]
    then
        return b - a
    break
    fi
def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
def test_sub():
    assert sub(1,2) == 1
    assert sub(-1,-2) == 1
