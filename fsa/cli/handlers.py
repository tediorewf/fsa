from functools import wraps

from fsa.exceptions import FiniteStateAutomataError


def catch_finite_state_automata_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FiniteStateAutomataError as err:
            message = str(err)
            print(message)
    return wrapper
