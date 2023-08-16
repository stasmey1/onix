def arrays_descending(a: list, b: list) -> list:
    a.extend(b)
    return sorted(a, reverse=True)

