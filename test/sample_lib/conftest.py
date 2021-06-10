import pytest


@pytest.fixture(autouse=True, scope="session")
def sample_fixture():
    return [x for x in range(10) if x % 2 == 0]
