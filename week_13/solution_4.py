# Exercises and Solutions by Nicholas Bertollo

from typing import Self

class State:
    """
    This represents a state in a finite state machine.
    It holds the state ID, and set of tuples which contain
    a character, such as 'a' and state ID.
    """
    def __init__(self, transitions: set[tuple[str]]):
        """
        If any of the strings in the tuple aren't a single character
        then throw a ValueError. 
        Otherwise the class should have attributes:
            transitions :: set[tuple[str, State]] :: Contains all the infomation for the transitions from this stata
        """
        for character, state in transitions:
            if len(character) != 1:
                raise ValueError(f"{character!r} is not a single character")
        self.transitions: set[tuple[str]] = transitions
    
    def add_transition(self, transition: tuple[str]):
        """
        Adds a transitions to our set of transitions. 
        throws a ValueError if the string isn't a single character.
        """
        if len(transition[0]) != 1:
            raise ValueError
        self.transitions.add(transition)

    def local_alphabet(self) -> str:
        """
        Finds and returns the string containing all the
        characters that can be transitions from
        """
        local_alphabet: str = ""
        for character, _ in self.transitions:
            if character not in local_alphabet:
                local_alphabet += character
        return local_alphabet

    def __str__(self) -> str:
        """
        Implement your own str methods for bug testing purposes. 
        """
        output_string: str = ""
        for character, _ in self.transitions:
            output_string += character
        return output_string
    
    def __repr__(self) -> str:
        return str(self)

class FiniteStateMachine:
    """
    This represents a finite state machine. 
    The idea is that given a string, we want to 
    either accept or reject that string according to 
    the state machine.
    More information:
    https://en.wikipedia.org/wiki/Finite-state_machine#Acceptors
    """
    def __init__(self, alphabet: str, start_state: State, states: set[State], final_states: set[State]):
        """
        If the alphabet is empty then throw a ValueError
        If the start_state isn't in the set of states, then throw a ValueError. 
        If any of the final states aren't in the set of states, then throw a ValueError.
        If the set of states is empty then throw a ValueError.
        If any of the transitions contain a character which isn't within the alphabet, then throw a ValueError.
        These should have good error messages.

        There should be attributes alphabet, start_state, and final_states.
        There should also be another attribute called language
            language is a set which is initially empty
        """
        if len(alphabet) == 0:
            raise ValueError
        
        if len(states) == 0:
            raise ValueError
        elif start_state not in states:
            raise ValueError
        elif not states.issuperset(final_states):
            raise ValueError
        for state in states:
            for character, _ in state.transitions:
                if len(character) != 1:
                    raise ValueError
        self.alphabet: str = alphabet
        self.start_state: State = start_state
        self.final_states: set[State] = final_states
        self.language: set[str] = set()
    
    def perform_run(self, input_string: str) -> bool:
        """
        This determines whether the given input_string is accepted or rejected
        from the FiniteStateMachine by the following rules:
        
        It considers the characters in the input_string from left to right, and
        the idea is to transition from one state to another depending on each character
        and state. 
        This is done until the whole input string is taken up, in which case we 
        accept the string if we end on a final state and we reject if
        we don't. 
        If the character doesn't exist within the local alphabet, then 
        this is an auto reject. 
        If we accept, we add this to self.language.
        """
        current_state: State = self.start_state
        for character in input_string:
            if character not in current_state.local_alphabet():
                return False

            for transition_character, next_state in current_state.transitions:
                if transition_character == character:
                    current_state: str = next_state
        
        if current_state not in self.final_states:
            return False
        
        self.language.add(input_string)
        return True
            
def main():
    state_0: State = State(set())
    state_1: State = State({('0', state_0)})
    state_0.add_transition(('1', state_1))
    state_0.add_transition(('0', state_0))
    state_1.add_transition(('1', state_1))

    machine: FiniteStateMachine = FiniteStateMachine("01", state_1, {state_0, state_1}, {state_0})
    """
    Note. This FiniteStateMachine specifically only accepts
    strings which end in 0. And so the language of this 
    FiniteStateMachine contains all the 
    """
    print(machine.perform_run("0101010"))
    print(machine.perform_run("01010"))
    print(machine.perform_run("010111111110"))
    print(machine.perform_run("010100000110"))
    print(machine.perform_run("0101010000011010110001"))
    print(machine.perform_run(""))
    print(machine.perform_run("1"))
    print(machine.perform_run("0"))
    print(machine.language)

if __name__ == "__main__":
    main()
