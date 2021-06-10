from unittest import TestCase
from unittest.main import main
from sample_lib.doctest_sample import foo_function


class DocktestSmapleTestCase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_foo_function(self):
        assert foo_function(2) == 4
        assert foo_function(3) == 9


if __name__ == "__main__":
    import sys
    print(sys.path)
    main()
