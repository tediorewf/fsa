from queue import Queue

import yaml

from . import const
from .exceptions import FiniteStateAutomataError, catch_os_error, catch_yaml_error


class FiniteStateAutomata:
    def __init__(self,
                 states: 'set[str]',
                 alphabet: 'set[str]',
                 transitions: 'dict[str, dict[str, set[str]]]',
                 starting_state: str,
                 final_states: 'set[str]'):
        if starting_state not in states:
            message = 'States do not contain starting state'
            raise FiniteStateAutomataError(message)

        if final_states.intersection(states) != final_states:
            message = 'Final states do not included in all states'
            raise FiniteStateAutomataError(message)
        
        self.__ensure_transitions_valid(transitions)
        
        self.__states = states
        self.__alphabet = alphabet
        self.__transitions = transitions
        self.__starting_state = starting_state
        self.__final_states = final_states

        self.__determined = False

    @classmethod
    def load_from_yaml(cls, filename: str) -> 'FiniteStateAutomata':
        params = FiniteStateAutomata.__parse_params_from_yaml(filename)
        return cls(**params)

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

    def to_dict(self) -> dict:
        d = {
            const.STATES: self.states,
            const.ALPHABET: self.alphabet,
            const.TRANSITIONS: self.transitions,
            const.STARTING_STATE: self.starting_state,
            const.FINAL_STATES: self.final_states
        }
        return d

    def determine(self) -> None:
        if self.__determined:
            return

        states = set()
        transitions = {}
        starting_group = {self.__starting_state}
        starting_state = FiniteStateAutomata.__set_to_state(starting_group)
        final_states = set()

        q = Queue()
        q.put(starting_group)

        while not q.empty():
            group = q.get()
            current_state = FiniteStateAutomata.__set_to_state(group)
            states.add(current_state)

            # Проверяем, финальная ли группа.
            if self.final_states.intersection(group):
                final_states.add(current_state)

            transitions[current_state] = {}

            # Проходим по каждому символу алфавита и добавляем в очередь группу состояний,
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
        self.__starting_state = starting_state
        self.__transitions = transitions
        self.__final_states = final_states

        self.__determined = True

    @staticmethod
    def __set_to_state(states: 'set[str]') -> str:
        state = '{' + ', '.join(sorted(s for s in states)) + '}'
        return state

    @staticmethod
    def __state_to_set(state: str) -> 'set[str]':
        return {state}

    @staticmethod
    def __ensure_transitions_valid(transitions: 'dict[str, dict[str, set[str]]]') -> None:
        pass

    @staticmethod
    @catch_yaml_error
    @catch_os_error
    def __parse_params_from_yaml(filename: str) -> dict:
        states: set = set()
        alphabet: set = set()
        transitions: 'dict[str, dict[str, set[str]]]' = {}
        starting_state: str = ''
        final_states: set = set()

        with open(filename, 'r') as f:
            data_loaded = yaml.safe_load(f)

            states = FiniteStateAutomata.__parse_states(data_loaded)
            alphabet = FiniteStateAutomata.__parse_alphabet(data_loaded)
            transitions = FiniteStateAutomata.__parse_transitions(data_loaded)
            starting_state = FiniteStateAutomata.__parse_starting_state(data_loaded)
            final_states = FiniteStateAutomata.__parse_final_states(data_loaded)

        params = {
            const.STATES: states,
            const.ALPHABET: alphabet,
            const.TRANSITIONS: transitions,
            const.STARTING_STATE: starting_state,
            const.FINAL_STATES: final_states
        }

        return params

    @staticmethod
    def __parse_states(data_loaded: dict) -> 'set[str]':
        states = set([str(state) for state in data_loaded[const.STATES]])
        return states

    @staticmethod
    def __parse_alphabet(data_loaded: dict) -> 'set[str]':
        alphabet = set([str(symbol) for symbol in data_loaded[const.ALPHABET]])
        return alphabet
    
    @staticmethod
    def __parse_transitions(data_loaded: dict) -> 'dict[str, dict[str, set[str]]]':
        transitions = {}

        for (state, transition) in data_loaded[const.TRANSITIONS].items():
            state = str(state)
            transitions[state] = {}

            for (symbol, states) in transition.items():
                states = set([str(state) for state in states])
                transitions[state][symbol] = states

        return transitions

    @staticmethod
    def __parse_starting_state(data_loaded: dict) -> str:
        starting_state = str(data_loaded[const.STARTING_STATE])
        return starting_state

    @staticmethod
    def __parse_final_states(data_loaded: dict) -> 'set[str]':
        final_states = set([str(state) for state in data_loaded[const.FINAL_STATES]])
        return final_states
