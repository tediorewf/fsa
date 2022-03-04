from functools import wraps

from fsa.exceptions import FiniteStateAutomataError


def handle_finite_state_automata_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FiniteStateAutomataError as err:
            print(err)
    return wrapper
