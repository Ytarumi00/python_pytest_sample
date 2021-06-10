import pytest
from sample_lib import sample


@pytest.mark.parametrize(("nums", "expected"), [
    ([1, 2, 3, 4, 5, 3], 18),
    ([1, 2, 3, 4, 5, 3], 19)  # error
])
def test_sample_1(nums, expected):
    assert sample.sum(*nums) == expected
