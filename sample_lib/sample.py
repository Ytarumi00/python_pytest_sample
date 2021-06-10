

from functools import reduce


def sum(*args, **kwargs):
    print(*args)
    return reduce(lambda x, y: x+y, [*args])


if __name__ == "__main__":  # pragma: no cover
    print(sum(1, 23, 4, 6,))
