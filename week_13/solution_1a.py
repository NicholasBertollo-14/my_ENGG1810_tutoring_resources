from typing import Self

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
        If there are n strands, then you cannot cross the (n - 1)-th strand
        across the n-th strand, this would be considered an 
        impossible crossing. 
        """
        if no_strands < 0:
            raise ValueError(f"{no_strands} is negative!")
        self.no_strands: int = no_strands
        for strand_index, _ in crossings: # _ just means we don't care about the crossing_type
            if strand_index < 0 or strand_index >= no_strands:
                raise ValueError("You cannot cross the {strand_index}-th strand over the {strand_index + 1}-th strand")
        self.crossings: list[tuple[int, bool]] = crossings

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
        Here is a couple more examples:
            [(1, True), (2, False), (2, True), (1, False)] -> []
            [(1, True), (3, False), (1, True)] -> [(1, True), (3, False), (1, True)]
        I would recommend you complete is_simplified first. 

        Note: This does not simplify real braids completely. 
        """
        while not self.is_simplified():
            for index, (strand_index, crossing_type) in enumerate(self.crossings[:-1]):
                next_strand_index, next_crossing_type = self.crossings[index + 1]
                if strand_index == next_strand_index and crossing_type is not next_crossing_type:
                    self.crossings.pop(index + 1)
                    self.crossings.pop(index)
                    break

    def is_simplified(self) -> bool:
        """
        Determines whether the current braid is fully simplified
        according to the rules of the function simplify. 
        """
        for index, (strand_index, crossing_type) in enumerate(self.crossings[:-1]):
            next_strand_index, next_crossing_type = self.crossings[index + 1]
            if strand_index == next_strand_index and crossing_type is not next_crossing_type:
                return False
        return True
    
    def stack(self, other_braid: Self):
        """
        This changes the current braid such that we stack 
        other_braid on top of the current braid. 
        This braid is then simplified. 
        If the number of strands in other_braid is different to
        the number of strands in the current braid, then
        throw a ValueError. 
        """
        if self.no_strands != other_braid.no_strands:
            raise ValueError("Cannot stack braids of different amount of strands")
        self.crossings: list[tuple[int, bool]] = self.crossings + other_braid.crossings
        self.simplify()
    
    def inverse(self) -> Self:
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
        inverse_braid = Braid(self.no_strands, [])
        for strand_index, crossing_type in reversed(self.crossings):
            inverse_braid.crossings.append((strand_index, not crossing_type))
        inverse_braid.simplify()
        return inverse_braid