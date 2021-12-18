""" pytest checkers """
import pytest


@pytest.mark.Regression
def test_addition():
    """

    :return:
    """
    assert 2+2 == 4


@pytest.mark.Sanity
@pytest.mark.parametrize('num, result', [(1, 10), (2, 20), (3, 35)])
def test_multiplication(num, result):
    """

    :param num:
    :param result:
    :return:
    """
    num = num * 10
    assert num == result
