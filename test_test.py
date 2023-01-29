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


def test_my_foo():
    """Test my_foo."""
    assert my_foo(four()) == 7


def test_function():
    """Test function."""
    assert function(3, four()) == 7
