"""pytestを使ったテストのサンプル


"""


from datetime import date, datetime, timedelta
from freezegun import freeze_time
import pytest


def test_sample01_success():
    """成功テスト
    """

    assert 1 == 1


def test_sample01_error():
    """失敗テスト
    """

    assert 1 == 2


def test_sample01_raise():
    """例外テスト
    """

    with pytest.raises(ValueError):
        raise ValueError


def test_sample01_raise_diff():
    """例外テスト失敗
    """

    with pytest.raises(ValueError):
        raise KeyError


@pytest.mark.skip
def test_skip():
    """skip mark
    アノテーションでテストのスキップをできる
    """
    assert 1 == 2


def is_even(num):
    """パラメータテスト用メソッド

    引数が偶数かを判定する

    Args:
        num ([int]): 引数

    Returns:
        [boolean]: 判定結果
    """
    return True if num % 2 == 0 else False


@pytest.mark.parametrize(('number', 'expected'), [
    (1, False),
    (2, True),
    (3, True),  # error
    (111, False),
    (112, True),
    (113, True)  # error
])
def test_parameter(number, expected):
    assert is_even(number) == expected


class Fruit:
    """fixture テスト用クラス
    """

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


# fixtureを設定
@pytest.fixture
def my_fruit():
    return Fruit("apple")

# fixtureを設定


@pytest.fixture
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]


def test_my_fruit_in_basket(my_fruit, fruit_basket):
    """fixtureを使ったテスト実行

    Args:
        my_fruit (Fruit):
        fruit_basket (list[Fruit]):
    """
    assert my_fruit in fruit_basket


# fixtureを使った後処理のテスト
class Client(object):
    def connect(self):
        print("--connect--")

    def send(self, msg):
        print("--send--{}".format(msg))

    def close(self):
        print("--close--")


# fixtureを使った後処理のテスト
@pytest.fixture
def client():
    # -- 前処理　
    client = Client()
    client.connect()

    # テスト実行
    yield client

    # -- 後処理
    client.close()


# fixtureを使った後処理のテスト
def test_sample(client):
    client.send('message')


@pytest.mark.usefixtures("sample_fixture1")
class TestSample:
    # conftest.pyで設定したfixtureをclassでまとめて複数のテストに実行
    # 成功する
    def test_sampole_1(self, sample_fixture1):
        assert 2 in sample_fixture

    # 失敗する
    def test_sampole_2(self, sample_fixture1):
        assert 1 in sample_fixture


class UnfinishedClass:
    """ Mockテストのサンプルクラス
    """
    def foo():
        pass


def test_mock(monkeypatch):
    """Mockテストを実行

    Args:
        monkeypatch ([type]): Mockテストメソッドには引数にこれを指定する
    """
    def run_mock(arg):
        return 3

    # monkeypatchを利用してメソッド差し替え(lamdbaを使ってもできる)
    monkeypatch.setattr(UnfinishedClass, "foo", run_mock)
    sut = UnfinishedClass()
    assert 3 == sut.foo()


def test_freeze_time():
    """時間指定してテスト
    """
    now = datetime.now()

    with freeze_time(now) as frozen_time:
        assert datetime.now() == now
        frozen_time.tick(timedelta(seconds=1))
        assert datetime.now() == now + timedelta(seconds=1)
