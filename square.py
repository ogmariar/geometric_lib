def area(a):
    if not isinstance(a, (int, float)):
        raise TypeError("Side length must be a real number.")
    if a < 0:
        raise ValueError("Side length cannot be negative.")
    return a ** 2

def perimeter(a):
    if not isinstance(a, (int, float)):
        raise TypeError("Side length must be a real number.")
    if a < 0:
        raise ValueError("Side length cannot be negative.")
    return 4 * a

