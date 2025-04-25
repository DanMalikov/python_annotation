from typing import Callable, Awaitable, ClassVar, Tuple, TypeVar, Literal, LiteralString, Iterable, TypedDict, \
    NotRequired, Required, Unpack


def run_async(x: Awaitable[int]):
    """
    Intermediate.await
    :return:
    """
    pass


SingleStringInput = Callable[[str], None]  # Intermediate.Callable


class Fooo:
    """Intermediate.ClassVar"""
    bar: ClassVar[int]


T = TypeVar("T", bound = Callable)
def decorator(func: T) -> T:
    """Intermediate.Decorator"""
    return func


EmptyTuple = Tuple[()]

def foo_empty_tuple(x: EmptyTuple):
    """Intermediate.EmptyTuple"""
    pass


Q = TypeVar("Q")

def add_generic1(a: Q, b: Q) -> Q:
    """Intermediate.Generic"""
    return a


Z = TypeVar("Z", int, str)

def add_generics2(a: Z, b: Z) -> Z:
    """Intermediate.Generic2"""
    return a


V = TypeVar("V", bound = int)

def add_generics3(a: V) -> V:
    """Intermediate.Generic3"""
    return a


class Foo:
    """Intermediate.instance_var"""
    bar: int


Side = Literal["left", "right"]

def foo_literal(direction: Side):
    """Intermediate.Literal"""
    ...


def execute_query(sql: LiteralString, parameters: Iterable[str] = ...):
    """Intermediate.Literalstring"""
    ...


class FooSelf:
    def return_self(self):
        """Intermediate.self"""
        return self


class Student1(TypedDict):
    """Intermediate.TypedDict"""
    name: str
    age: int
    school: str


class Student2(TypedDict):
    """Intermediate.TypedDict2"""
    name: str
    age: int
    school: NotRequired[str]


class Person(TypedDict, total=False):
    """Intermediate.TypedDict3"""
    name: Required[str]
    age: int
    gender: str
    address: str
    email: str


class Person2(TypedDict):
    """Intermediate.Unpack"""
    name: str
    age: int


def foo(**kwargs: Unpack[Person]):
    ...
