"""
Representing a SR flip-flop as a finite state machine
"""

from transition import Transition, FSM

# The set of states
states = ['Q=0', 'Q=1', 'Error']

# the set of allowed inputs
# These represent possible permutations of S and R
alphabet = ['00', '01', '10', '11']

# The set of accepted states
accepting_states = ['Q=0', 'Q=1']

# The initial state
initial_state = 'Q=0'

# Create the FSM
fsm = FSM(states, alphabet, accepting_states, initial_state)

# Create transitions
transition1 = Transition('Q=0', '00', 'Q=0')
transition2 = Transition('Q=0', '01', 'Q=0')
transition3 = Transition('Q=0', '10', 'Q=1')
transition4 = Transition('Q=0', '11', 'Error')
transition5 = Transition('Q=1', '00', 'Q=1')
transition6 = Transition('Q=1', '01', 'Q=0')
transition7 = Transition('Q=1', '10', 'Q=1')
transition8 = Transition('Q=1', '11', 'Error')
transition9 = Transition('Error', '00', 'Error')
transition10 = Transition('Error', '01', 'Error')
transition11 = Transition('Error', '10', 'Error')
transition12 = Transition('Error', '11', 'Error')
transitions = [
    transition1,
    transition2,
    transition3,
    transition4,
    transition5,
    transition5,
    transition6,
    transition7,
    transition8,
    transition9,
    transition10,
    transition11,
    transition12]

# Verify transitions add them to the FSM
fsm.add_transitions(transitions)

# Now that the FSM is correctly set up, give it some input to process
# This sequence represents the sequence:  Set, Reset, Set, do nothing, invalid input
# run_machine = fsm.accepts(['10', '01', '10', '00', '11'])

run_machine = fsm.accepts(['01', '10', '00', '01', '10'])


print('Final state is legal:', run_machine)
