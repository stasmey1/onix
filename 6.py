import random


def missing_number() -> int:
    list_ = [_ for _ in range(1, 1_000)]
    list_.pop(random.randint(1, 1_000))
    random.shuffle(list_)
    for i, v in enumerate(list_):
        k = v + 1
        if k not in list_ and v != max(list_):
            return k
