"""Test doc test doc."""
from json import dumps
from yaml import safe_load


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
    with open(".pre-commit-config.yaml", encoding="utf-8") as yaml_file:
        data = safe_load(yaml_file)
    print(dumps(data, indent=4))
