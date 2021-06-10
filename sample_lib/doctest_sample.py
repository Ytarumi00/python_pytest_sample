"""docstringのテストモジュール

"""

import functools
import pprint


def foo_decorator(f):
    import logging
    logger = logging.getLogger(__name__)

    @functools.wraps(f)
    def foo_wrapper(*args, **kwargs):
        logger.debug("args: {}".format(args))
        return f(*args, **kwargs)
    return foo_wrapper


@foo_decorator
def foo_function(*args):
    """デコってる関数のDocstring

    引数の２乗を返却する

    Args:
      n(int): 数値
    Return:
      int: 引数を２乗した値

    Examples:
      >>> foo_function(2)
      4
      >>> foo_function(2,2)
      4

    """
    return args[0] ** 2


if __name__ == '__main__':  # pragma: no cover
    import doctest
    import logging
    logging.basicConfig(level=logging.DEBUG, handlers=[
                        logging.StreamHandler()])
    doctest.testmod(verbose=True)
