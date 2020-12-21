from transition import Transition, FSM

# Set up our FSM with the required info:
# Set of states
states = ['State 1', 'State 2', 'Error']
# Set of allowed inputs
alphabet = [1, 0]
# Set of accepted states
accepting_states = ['State 1']
# The initial state
initial_state = 'State 1'
fsm = FSM(states, alphabet, accepting_states, initial_state)

# Create the set of transitions
transition1 = Transition('State 1', 1, 'State 2')
transition2 = Transition('State 2', 0, 'State 1')
transition3 = Transition('State 1', 0, 'Error')
transition4 = Transition('State 2', 1, 'Error')
transition5 = Transition('Error', 1, 'Error')
transition6 = Transition('Error', 0, 'Error')
transitions = [
    transition1,
    transition2,
    transition3,
    transition4,
    transition5,
    transition6]
# Verify and add them to the FSM
fsm.add_transitions(transitions)

# Now that our FSM is correctly set up, we can give it input to process
# Let's transition the FSM to a green light
should_be_accepted = fsm.accepts([1, 0, 1, 0])
print(should_be_accepted)

# Let's transition the FSM to a red light
should_be_rejected_1 = fsm.accepts([1, 1, 1, 0])
print(should_be_rejected_1)

# Let's transition to yellow and give it bad input
should_be_rejected_2 = fsm.accepts([1, 0, 1, 0, 1, 0, 0])
print(should_be_rejected_2)