

from functools import reduce


def sample(*args, **kwargs):
    print(*args)
    return reduce(lambda x, y: x+y, [*args])


if __name__ == "__main__":
    print(sample(1, 23, 4, 6,))
