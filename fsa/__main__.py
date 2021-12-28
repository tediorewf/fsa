from . import fsa

states = {
    '1', '2', '3'
}

alphabet = {
    'a', 'b'
}

transitions = {
    '1': {
        'a': {'1', '2'},
        'b': {'3'},
    },
    '2': {
        'a': {'2'},
        'b': {'1', '3'}
    },
    '3': {
        'a': {'3'},
        'b': {'3'}
    }
}

starting_state = '1'

final_states = {
    '3'
}

machine = fsa.FiniteStateAutomata(
    states=states,
    alphabet=alphabet,
    transitions=transitions,
    starting_state=starting_state,
    final_states=final_states,
)

print(machine)

machine = fsa.FiniteStateAutomata.load_from_yaml('./examples/fsa-non-det1.yaml')
print(machine)

machine.determine()
print(machine.transitions)
