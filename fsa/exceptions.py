from functools import wraps

from yaml import YAMLError


def catch_yaml_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except YAMLError as err:
            raise ParamsParsingError(err)
    return wrapper


class FiniteStateAutomataError(Exception):
    pass


class ParamsParsingError(FiniteStateAutomataError):
    pass


def catch_finite_state_automata_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FiniteStateAutomataError as err:
            message = str(err)
            print(message)
    return wrapper
