import pytest
from src.main import add_numbers


def test_add_numbers():
    assert add_numbers(1, 2) == 3
    assert add_numbers(-1, 2) == 1
    assert add_numbers(0, 0) == 0
    assert add_numbers(100, 200) == 300
    assert add_numbers(-100, -200) == -300
