from typing import Callable, Awaitable, ClassVar, Tuple, TypeVar, Literal, LiteralString, Iterable, TypedDict, \
    NotRequired, Required, Unpack


def run_async(x: Awaitable[int]):
    """
    Intermediate.async
    :return:
    """
    pass


SingleStringInput = Callable[[str], None]  # Intermediate.Callable


class Fooo:
    """Hint: No need to write __init__"""
    bar: ClassVar[int]


T = TypeVar("T", bound = Callable)
def decorator(func: T) -> T:
    return func


EmptyTuple = Tuple[()]

def foo_empty_tuple(x: EmptyTuple):
    pass


Q = TypeVar("Q")

def add_generic1(*args: Q) -> Q:
    pass


Z = TypeVar("Z", int, str)

def add_generics2(*args: Z) -> Z:
    ...


V = TypeVar("V", bound = int)

def add_generics3(a: V) -> V:
    ...


class Foo:
    """Hint: you don't need to write __init__"""
    bar: int


Side = Literal["left", "right"]

def foo_literal(direction: Side):
    ...


def execute_query(sql: LiteralString, parameters: Iterable[str] = ...):
    ...


class FooSelf:
    def return_self(self):
        return self


class Student1(TypedDict):
    name: str
    age: int
    school: str


class Student2(TypedDict):
    name: str
    age: int
    school: NotRequired[str]


class Person(TypedDict, total=False):
    name: Required[str]
    age: int
    gender: str
    address: str
    email: str


class Person2(TypedDict):
    name: str
    age: int


def foo(**kwargs: Unpack[Person]):
    ...
