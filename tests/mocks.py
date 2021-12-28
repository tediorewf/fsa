from fsa import const

_fsa_non_det_mock1_states = {'1', '2', '3'}
_fsa_non_det_mock1_alphabet = {'a', 'b'}
_fsa_non_det_mock1_transitions = {
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
_fsa_non_det_mock1_starting_state = '1'
_fsa_non_det_mock1_final_states = {'3'}

fsa_non_det_mock1_params = {
    const.STATES: _fsa_non_det_mock1_states,
    const.ALPHABET: _fsa_non_det_mock1_alphabet,
    const.TRANSITIONS: _fsa_non_det_mock1_transitions,
    const.STARTING_STATE: _fsa_non_det_mock1_starting_state,
    const.FINAL_STATES: _fsa_non_det_mock1_final_states,
}

_fsa_det_mock1_states = {
    '{1}', '{3}', '{1, 2}', '{1, 3}', '{1, 2, 3}'
}
_fsa_det_mock1_alphabet = {'a', 'b'}
_fsa_det_mock1_transitions = {
    '{1}': {
        'b': {'{3}'},
        'a': {'{1, 2}'}
    },
    '{3}': {
        'b': {'{3}'},
        'a': {'{3}'}
    },
    '{1, 2}': {
        'b': {'{1, 3}'},
        'a': {'{1, 2}'}
    },
    '{1, 3}': {
        'b': {'{3}'},
        'a': {'{1, 2, 3}'}
    },
    '{1, 2, 3}': {
        'b': {'{1, 3}'},
        'a': {'{1, 2, 3}'}
    }
}
_fsa_det_mock1_starting_state = '{1}'
_fsa_det_mock1_final_states = {
    '{1, 3}', '{1, 2, 3}', '{3}'
}

fsa_det_mock1_params = {
    const.STATES: _fsa_det_mock1_states,
    const.ALPHABET: _fsa_det_mock1_alphabet,
    const.TRANSITIONS: _fsa_det_mock1_transitions,
    const.STARTING_STATE: _fsa_det_mock1_starting_state,
    const.FINAL_STATES: _fsa_det_mock1_final_states,
}
