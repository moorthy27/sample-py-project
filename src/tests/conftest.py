import pytest

from codeToTest.basket import Basket


@pytest.fixture
def basket():
    b = Basket(count=1, capacity=10)
    return b
