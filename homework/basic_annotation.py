from typing import Any, Dict, Final, List, Optional, Tuple, Union


def foo_any(value: Any):
    """
    Basic.Any
    :param value:
    :return:
    """
    pass


def foo_dict(value: Dict[str, str]):
    """
    Basic.Dict
    :param value:
    :return:
    """
    pass


# Basic.Final
my_list: Final[List[int]] = []


def foo_kwargs(**kwargs: str | int):
    """
    Basic.kwargs
    :param kwargs:
    :return:
    """
    pass


def foo_list(x: List[str]):
    """
    Basic.List
    :param x:
    :return:
    """
    pass


def foo_optional(x: Optional[int | None] = None):
    """
    Basic.Optional
    :param x:
    :return:
    """
    pass


def foo_parameter(x: int):
    """
    Basic.parameter
    :param x:
    :return:
    """
    pass


def foo_return() -> int:
    """
    Basic.return
    :return:
    """
    return 1


def foo_tuple(x: Tuple[str,int]):
    """
    Basic.Tuple
    :param x:
    :return:
    """
    pass


Vector = List[float]  # Basic.Typealias


def foo_union(x: Union[str, int]):
    """
    Basic.Union
    :param x:
    :return:
    """
    pass




