from lib.module import say_hello, MyClass


def test_configurable_function():
    # at runtime
    say_hello()
    # registrate config for publishing package
    say_hello(registrate_config=True)

    MyClass()
    MyClass(registrate_config=True)

