import pytest


def test_initial_count(basket):
    assert basket.count == 1


def test_add_item(basket):
    basket.add_item(2)
    assert basket.count == 3


def test_add_raises_error(basket):
    with pytest.raises(ValueError) as e:
        basket.add_item(10)
    assert "Reached Max Capacity" in str(e.value)


def test_remove_raises_error(basket):
    with pytest.raises(ValueError) as e:
        basket.remove_item(10)
    assert "No items to remove" in str(e.value)


def test_remove_item(basket):
    basket.remove_item(1)
    assert basket.count == 0
