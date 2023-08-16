def f(a) -> int:
    res = 1
    for i, v in enumerate(a):
        if i == 2:
            return res * i
