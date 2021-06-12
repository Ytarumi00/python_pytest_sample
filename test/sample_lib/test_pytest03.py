import pytest
import itertools
from sample_lib import sample


@pytest.mark.parametrize(("nums", "expected"), [
    ([1, 2, 3, 4, 5, 3], 18),
    ([1, 2, 3, 4, 5, 3], 19)  # error
])
def test_sample_1(nums, expected):
    """パラメータを利用した外部ファイルのテスト

    """
    assert sample.sum(*nums) == expected


def generate_testcase():
    foo = list(itertools.product((1, 2, 3), (4, 5, 6)))
    bar = [x[0]+x[1] for x in foo]
    return zip(foo, bar)


@pytest.mark.parametrize(("nums", "expected"), generate_testcase())
def test_sample_2(nums, expected):
    """パラメータ作成部分を関数化
    """
    assert sample.sum(*nums) == expected


def test_sample_3(sample_fixture2):
    """fixtureを使って複数のテストケースを実行
    """
    num, expect = sample_fixture2
    assert sample.sum(*num) == expect
