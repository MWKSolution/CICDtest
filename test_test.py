"""Testing main."""
import pytest
from main import my_foo, function


@pytest.fixture
def four():
    """Four."""
    return 4


def test_always_pass():
    """Dummy test."""
    assert True


def test_my_foo(four):
    """Test my_foo."""
    arg = four
    assert my_foo(arg) == 7


def test_function(four):
    """Test function."""
    arg2 = four
    assert function(3, arg2) == 7
