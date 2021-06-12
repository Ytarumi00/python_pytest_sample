import pytest
import functools


@pytest.fixture(autouse=True, scope="session")
def sample_fixture1():
    return [x for x in range(10) if x % 2 == 0]


@pytest.fixture(params=[
    (1, 2, 3),
    (4, 5, 6)
])
def sample_fixture2(request):
    return (request.param,
            functools.reduce(lambda x, y: x+y, [*request.param]))
