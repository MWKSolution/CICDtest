"""Test doc test doc."""

# LOGIN = "login"
# PASSWD = "passwd"


def my_foo(foo_x: int) -> int:
    """Foo."""
    return foo_x + 3


def function(arg_a: float, arg_b: float) -> float:
    """Function."""
    print("Hello CICD")
    return arg_a + arg_b


if __name__ == "__main__":
    print(function(1, 2))
