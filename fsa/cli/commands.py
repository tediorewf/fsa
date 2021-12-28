from fsa.fsa import FiniteStateAutomata
from .handlers import catch_finite_state_automata_error


@catch_finite_state_automata_error
def determine(filename: str) -> None:
    automata = FiniteStateAutomata.load_from_yaml(filename)
    automata.determine()
    print(automata.to_dict())
