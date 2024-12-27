
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
    
    def add_transition(self, transition: tuple[str]):
        """
        Adds a transitions to our set of transitions. 
        throws a ValueError if the string isn't a single character.
        """

    def local_alphabet(self) -> str:
        """
        Finds and returns the string containing all the
        characters that can be transitions from
        """

    def __str__(self) -> str:
        """
        Implement your own str methods for bug testing purposes. 
        """
    
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
        If we accept, we add this to self.language and return True. 
        If we reject, we return False.
        """
            
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
