import sys
from typing import Any, NoReturn


def is_builtin(instance: Any) -> bool:
    return type(instance).__module__ == "builtins"


def print_vars() -> NoReturn:
    """
    Doesn't return anything, but rather prints the information about caller's local variables as a side effect 
    :return: 
    """
    frame = sys._getframe(1) 
    local_vars = frame.f_locals

    print()
    for var, instance in local_vars.items():
        print(f"{var}: {is_builtin(instance)}")
