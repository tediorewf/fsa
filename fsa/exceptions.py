from functools import wraps

from yaml import YAMLError


def handle_yaml_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except YAMLError as err:
            raise ParamsParsingError(err)
    return wrapper


def handle_os_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except OSError as err:
            raise ParamsParsingError(err)
    return wrapper


class FiniteStateAutomataError(Exception):
    pass


class ParamsParsingError(FiniteStateAutomataError):
    pass
