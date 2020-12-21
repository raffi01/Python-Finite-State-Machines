class MealyMachine(object):
    """Mealy Machine : Finite Automata with Output """

    def __init__(self, states, input_alphabet, output_alphabet, transitions, initial_state):
        """
        6 tuple (Q, ∑, O, δ, X, q0) where −

        states is a finite set of states.

        alphabet is a finite set of symbols called the input alphabet.

        output_alphabet is a finite set of symbols called the output alphabet.

        transitions is the resultant data dictionary of input and output transition functions

        initial_state is the initial state from where any input is processed (q0 ∈ Q).
        """
        self.states = states
        self.input_alphabet = input_alphabet
        self.output_alphabet = output_alphabet
        self.transitions = transitions
        self.initial_state = initial_state

    def get_output_from_string(self, string):
        """Return Mealy Machine's output when a given string is given as input"""

        temp_list = list(string)
        current_state = self.initial_state
        output = ''
        for x in temp_list:
            output+= self.transitions[current_state][x][1]
            current_state = self.transitions[current_state][x][0]

        return output


    def __str__(self):
        output = "\nMealy Machine" + \
                 "\nStates " + str(self.states) + \
                 "\nTransitions " + str(self.transitions) + \
                 "\nInital State " + str(self.initial_state) + \
                 "\nInput Alphabet " + str(self.input_alphabet) + \
                 "\nOutput Alphabet" + str(self.output_alphabet)

        return output


mealy = MealyMachine(
    ['a', 'b'],
    ['00', '01', '10', '11'],
    ['0', '1'],
    {
        'a' : {
            '00' : ('a', '0'),
            '01' : ('a', '1'),
            '10' : ('a', '1'),
            '11' : ('b', '0')
        },

        'b' : {
            '00' : ('a', '1'),
            '01' : ('b', '0'),
            '10' : ('b', '0'),
            '11' : ('b', '1')
        },
    },
    'a'
)

# build binary pairs to add
# include an extra leading 0 for each addend to allow for potential carry bit?
# This same functionality could be achieved by appending 0/1 for the last bit depending on state?


# s1 = "01"
# s2 = "01"

# s1 = "0101" # 5
# s2 = "0101" # 5
# Expect 1010 # 10

# s1 = "01010100000000000000101010101010101010011111111" # 5
# s2 = "01110111111110101010111100111100000000000001111" # 1
# Expect ?

s1 = "0001"
s2 = "0100"
# expect 0101

l1 = list(zip(s1, s2))
l2 = ["".join(tup) for tup in l1][::-1]

print(mealy)
print(mealy.get_output_from_string(l2)[::-1]) # Should be 1001001 (73)
