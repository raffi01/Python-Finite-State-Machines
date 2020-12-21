from transition import Transition, FSM

# Attempting to represent an SR latch (NAND)

# Set up our FSM with the required info:
# Set of states
states = ['Q=0', 'Q=1', 'Error']
# Set of allowed inputs
# These represent possible permutations of S and R
alphabet = ['00', '01', '10', '11']
# Set of accepted states
accepting_states = ['Q=0', 'Q=1']
# The initial state
initial_state = 'Q=0'
fsm = FSM(states, alphabet, accepting_states, initial_state)

# Create the set of transitions
# S = 0: set, R = 0: reset
transition1 = Transition('Q=0', '00', 'Error')
transition2 = Transition('Q=0', '01', 'Q=1')
transition3 = Transition('Q=0', '10', 'Q=0')
transition4 = Transition('Q=0', '11', 'Q=0')
transition5 = Transition('Q=1', '00', 'Error')
transition6 = Transition('Q=1', '01', 'Q=1')
transition7 = Transition('Q=1', '10', 'Q=0')
transition8 = Transition('Q=1', '11', 'Q=1')
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
# Verify and add them to the FSM
fsm.add_transitions(transitions)

# Now that our FSM is correctly set up, we can give it input to process
run_machine = fsm.accepts(['11', '01', '11', '00'])
print("Final state is legal:", run_machine)

# # Let's transition the FSM to a red light
# should_be_rejected_1 = fsm.accepts([1, 1, 1, 0])
# print(should_be_rejected_1)

# # Let's transition to yellow and give it bad input
# should_be_rejected_2 = fsm.accepts([1, 0, 1, 0, 1, 0, 0])
# print(should_be_rejected_2)