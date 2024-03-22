from functools import partial
from lib.config import configurable


@configurable
def say_hello(person_name: str = "John Doe"):
    print(f"\nHello {person_name}!")


@configurable
class MyClass(object):
    def __init__(self, init_argument: str = "default_value"):
        self.init_argument = init_argument




