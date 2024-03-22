# TODO: implement decorator for configurability:
# the decorator must handle both - classes and methods
# write arguments and default value types in dict
# object config should only be added to the config file if it's decorated with the corresponding decorator
import inspect


def configurable(obj):

    def inner(*args, **kwargs):
        if "registrate_config" in kwargs.keys():
            registrate_config = kwargs.get("registrate_config")
            kwargs.pop("registrate_config")
        else:
            registrate_config = False
        if not registrate_config:
            if inspect.isfunction(obj):
                obj(*args, **kwargs)
                func_handler = FunctionHandler(obj)
                print(f"I am a function. And this is my configuration: "
                      f"\n{func_handler.get_config()}")
            else:
                obj(*args, **kwargs)
                class_handler = ClassHandler(obj)
                print(f"I am a class. And this is my configuration: "
                      f"\n{class_handler.get_config()}")
        else:
            print("\nRegister config.")
    return inner


class FunctionHandler:
    def __init__(self, func):
        self.func = func

    def get_config(self):
        signature = inspect.signature(self.func)
        name = self.func.__name__
        config = {name: {}}
        for param_name, param in signature.parameters.items():
            if param.default != inspect.Parameter.empty:
                config[name][param_name] = (param.default, type(param.default))
        return config

    def set_config(self):
        pass


class ClassHandler:
    def __init__(self, cls):
        self.cls = cls

    def get_config(self):
        constuctor = inspect.signature(self.cls.__init__)
        name = self.cls.__name__
        config = {name: {}}
        for param_name, param in constuctor.parameters.items():
            if param.default != inspect.Parameter.empty:
                config[name][param_name] = (param.default, type(param.default))
        return config