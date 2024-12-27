import unittest

class TestingBraid(unittest.TestCase):
    """
    This tests the Braid class
    """
    
    def test_no_strands(self):
        """
        Test creating a Braid object with a varying number of strands.
        There should be at least 3 asserts, testing at least 2 edge cases. 
        It is your job to determine what the edge cases are. 
        """
    
    def test_crossings(self):
        """
        Test creating a Braid object with different lists of crossings. 
        There should  be at least 3 asserts, testing at least 3 edge cases. 
        It is your job to determine what the edge cases are. 
        """
    
    def test_is_simplified(self):
        """
        This tests the method is_simplify on a variety of braids. 
        You should compare the output of the method
        to some expected outputs you've calculated yourself. 
        There should be at least 3 asserts. 
        """


    def test_simplified(self):
        """
        This tests the method simplify on a variety of braids. 
        You should compare the output of the method
        to some expected outputs you've calculated yourself. 
        There should be at least 3 asserts. 
        """
    
    def test_stack(self):
        """
        This tests the method stack on a variety of braids. 
        You should compare the output of the method
        to some expected outputs you've calculated yourself. 
        There should be at least 3 asserts. 
        """

    def test_inverse(self):
        """
        This tests the method inverse on a variety of braids. 
        You should compare the output of the method
        to some expected outputs you've calculated yourself. 
        There should be at least 3 asserts. 
        """

if __name__ == "__main__":
    unittest.main()
