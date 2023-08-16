def min_max(a: int | float, b: int | float) -> tuple:
    a, b = min(a, b), max(a, b)
    return a, b
