
class Braid:
    """
    This represents the idea of a braid in 3D space. 
    This class specifically includes ideas that
    arrive from the braid group. 
        https://en.wikipedia.org/wiki/Braid_group
    This class doesn't include everything there is 
    to braids. 
    """
    def __init__(self, no_strands: int, crossings: list[tuple[int, bool]]):
        """
        Create attributes:
            no_strands :: which raises a ValueError if this is negative. 
            crossings  :: which raises a ValueError if it's an impossible crossing.

        Each crossing is in the form (strand_index, crossing_type). 
        The strand index starts at index 0, for the first braid. 
        If the crossing type is True, then this is an over crossing. 
        If the crossing type is False, then this is an under crossing. 

        Each strand_index is a number and represents crossing the i-th
        strand over the (i + 1)-th strand. 
        If there are n strands, then you cannot cross the n-th strand
        across the (n + 1)-th strand, this would be considered an 
        impossible crossing. 
        """

    def simplify(self):
        """
        This simplifies the braid into another braid by the following rules. 
        
        If we perform an overcrossing then an undercrossing on the 
        same strands, then these cancel out.
        If we perform an undercrossing then an overcrossing on the
        same strands, then these cancel out.  
        For example: [(1, True), (1, False), (1, True)] -> [(1, True)]

        Perform this simplification until the braid cannot be
        simplified further. 
        Here is one more example:
            [(1, True), (2, False), (2, True), (1, False)] -> []
        This does not return anything, it only changes the crossings in the braid. 
        """

    def is_simplified(self) -> bool:
        """
        Determines whether the current braid is fully simplified
        according to the rules of the function simplify. 
        """
        
    def stack(self, other_braid):
        """
        This changes the current braid such that we stack 
        other_braid on top of the current braid. 
        This braid is then simplified. 
        """
    
    def inverse(self):
        """
        Calculates and returns the inverse braid of the current braid. 
        The inverse should be in simplified form. 
        The inverse braid has the unique property such that:
            When we stack the inverse_braid into the current braid
            and simplify, we get the empty braid.  
        E.g. The inverse braid of:
            [(1, True), (2, False), (4, True), (5, False)] is
            [(5, True), (4, False), (2, True), (1, False)]  
        Note: We do not want to change any of the attributes of the current
        braid, we only want to return the inverse braid. 
        """