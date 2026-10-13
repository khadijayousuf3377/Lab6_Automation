
def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid input"

    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid triangle"

    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"


def test_equilateral():
    assert classify_triangle(3, 3, 3) == "Equilateral"


def test_isosceles():
    assert classify_triangle(3, 3, 4) == "Isosceles"


def test_scalene():
    assert classify_triangle(3, 4, 5) == "Scalene"


def test_invalid_triangle():
    assert classify_triangle(1, 1, 3) == "Invalid triangle"


def test_invalid_input():
    assert classify_triangle(0, 4, 5) == "Invalid input"


def test_another_isosceles():
    assert classify_triangle(5, 5, 8) == "Isosceles"
