"""pytestを使ったテストのサンプル

classでテストをまとめたもの

"""


import pytest


class TestGroup:

    def test_sample01_success(self):
        """成功テスト
        """

        assert 1 == 1

    def test_sample01_error(self):
        """失敗テスト
        """

        assert 1 == 2

    def test_sample01_raise(self):
        """例外テスト
        """

        with pytest.raises(ValueError):
            raise ValueError

    def test_sample01_raise_diff(self):
        """例外テスト失敗
        """

        with pytest.raises(ValueError):
            raise KeyError
