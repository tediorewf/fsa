from queue import Queue

from . import const, exceptions, utils


class FiniteStateAutomata:
    def __init__(self,
                 states: 'set[str]',
                 alphabet: 'set[str]',
                 transitions: 'dict[str, dict[str, set[str]]]',
                 starting_state: str,
                 final_states: 'set[str]'):
        self.__states = states
        self.__alphabet = alphabet
        self.__transitions = transitions
        self.__starting_state = starting_state
        self.__final_states = final_states

        self.__is_determined = False

    @property
    def states(self) -> 'set[str]':
        return self.__states

    @property
    def alphabet(self) -> 'set[str]':
        return self.__alphabet

    @property
    def transitions(self) -> 'dict[str, dict[str, set[str]]]':
        return self.__transitions

    @property
    def starting_state(self) -> str:
        return self.__starting_state

    @property
    def final_states(self) -> 'set[str]':
        return self.__final_states

    @property
    def is_determined(self) -> bool:
        return self.__is_determined

    @classmethod
    def load_from_file(cls, filename: str):
        states = set()
        alphabet = set()
        transitions = {}
        starting_state = ''
        final_states = set()
        return cls(states, alphabet, transitions, starting_state, final_states)

    def determine(self) -> None:
        if self.is_determined:
            return

        states = set()
        transitions = {}
        final_states = set()

        q = Queue()
        q.put({self.starting_state})

        while not q.empty():
            group = q.get()
            current_state = FiniteStateAutomata.__set_to_state(group)
            states.add(current_state)

            # Проверяем, финальная ли группа.
            if self.final_states.intersection(group):
                final_states.add(current_state)

            transitions[current_state] = {}

            # Проходимся по каждому символу алфавита и добавляем в очередь группу состояний,
            # которая может быть достигнута из состояний текущей группы.
            for symbol in self.alphabet:
                next_group = set()
                for state in group:
                    for s in self.transitions[state][symbol]:
                        next_group.add(s)

                if next_group:
                    next_state = FiniteStateAutomata.__set_to_state(next_group)
                    transitions[current_state][symbol] = FiniteStateAutomata.__state_to_set(next_state)

                    if next_state not in states:
                        q.put(next_group)

        self.__states = states
        self.__transitions = transitions
        self.__final_states = final_states

        self.__is_determined = True

    @staticmethod
    def __set_to_state(states: 'set[str]') -> str:
        return utils.replace_multiple(
            base=str(states),
            replaceables=const.SET_TO_STATE_REPLACEABLES,
            replacement=const.SET_TO_STATE_REPLACEMENT,
        )

    @staticmethod
    def __state_to_set(state: str) -> 'set[str]':
        return {state}
