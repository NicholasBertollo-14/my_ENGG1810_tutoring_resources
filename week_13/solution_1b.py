import unittest
from solution_1a import Braid

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
        for i in range(100):
            self.assertEqual(Braid(i, []).no_strands, i)
        self.assertEqual(Braid(1_000_000_000, []).no_strands, 1_000_000_000)
        self.assertRaises(ValueError, Braid, -10, [])
        self.assertRaises(ValueError, Braid, -1, [])
    
    def test_crossings(self):
        """
        Test creating a Braid object with different lists of crossings. 
        There should  be at least 3 asserts, testing at least 3 edge cases. 
        It is your job to determine what the edge cases are. 
        """
        self.assertRaises(ValueError, Braid, 10, [(10, True)])
        self.assertRaises(ValueError, Braid, 10, [(100, True)])
        self.assertRaises(ValueError, Braid, 10, [(-1, True)])
        self.assertIn((0, False), Braid(10, [(0, False)]).crossings)
        for i in range(100):
            self.assertIn((i, False), Braid(1000, [(i, False)]).crossings)
            self.assertNotIn((i, True), Braid(1000, [(i + 1, True)]).crossings)
            self.assertNotIn((i, True), Braid(1000, [(i, False)]).crossings)
    
    def test_is_simplified(self):
        """
        This tests the method is_simplify on a variety of braids. 
        You should compare the output of the method
        to some expected outputs you've calculated yourself. 
        There should be at least 3 asserts. 
        """
        self.assertFalse(Braid(100, [(1, True), (1, False)]).is_simplified())
        self.assertFalse(Braid(100, [(1, False), (1, True)]).is_simplified())
        self.assertTrue(Braid(100, [(1, True), (1, True)]).is_simplified())
        self.assertTrue(Braid(100, [(1, False), (1, False)]).is_simplified())
    
    def test_simplified(self):
        """
        This tests the method simplify on a variety of braids. 
        You should compare the output of the method
        to some expected outputs you've calculated yourself. 
        There should be at least 3 asserts. 
        """
        braid_1: Braid = Braid(100, [(1, True), (1, False)])
        braid_2: Braid = Braid(100, [(1, False), (1, True)])
        braid_3: Braid = Braid(100, [(1, True), (1, True)])
        braid_4: Braid = Braid(100, [(1, False), (1, False)])
        braid_5: Braid = Braid(100, [(1, True), (3, False), (1, True)])
        braid_6: Braid = Braid(100, [(1, True), (1, False), (1, True)])

        braid_1.simplify()
        braid_2.simplify()
        braid_3.simplify()
        braid_4.simplify()
        braid_5.simplify()
        braid_6.simplify()

        self.assertEqual(braid_1.crossings, [])
        self.assertEqual(braid_2.crossings, [])
        self.assertEqual(braid_3.crossings, [(1, True), (1, True)])
        self.assertEqual(braid_4.crossings, [(1, False), (1, False)])
        self.assertEqual(braid_5.crossings, [(1, True), (3, False), (1, True)])
        self.assertEqual(braid_6.crossings, [(1, True)])
    
    def test_stack(self):
        """
        This tests the method stack on a variety of braids. 
        You should compare the output of the method
        to some expected outputs you've calculated yourself. 
        There should be at least 3 asserts. 
        """
        braid_1: Braid = Braid(100, [(1, True), (1, False)])
        braid_2: Braid = Braid(100, [(1, False), (1, True)])
        braid_3: Braid = Braid(100, [(1, True), (1, True)])
        braid_4: Braid = Braid(100, [(1, False), (1, False)])
        braid_5: Braid = Braid(100, [(1, True), (3, False), (1, True)])
        braid_6: Braid = Braid(100, [(1, True), (1, False), (1, True)])

        braid_1.stack(braid_2)
        braid_3.stack(braid_4)
        braid_5.stack(braid_6)


        self.assertEqual(braid_1.crossings, [])
        self.assertEqual(braid_3.crossings, [])
        self.assertEqual(braid_5.crossings, [(1, True), (3, False), (1, True), (1, True)])

    def test_inverse(self):
        """
        This tests the method inverse on a variety of braids. 
        You should compare the output of the method
        to some expected outputs you've calculated yourself. 
        There should be at least 3 asserts. 
        """
        braid_1: Braid = Braid(100, [(1, False), (1, False)])
        braid_2: Braid = Braid(100, [(1, True), (3, False), (1, True)])
        braid_3: Braid = Braid(100, [(2, True), (1, False), (3, True)])

        self.assertEqual(braid_1.inverse().crossings, [(1, True), (1, True)])
        self.assertEqual(braid_2.inverse().crossings, [(1, False), (3, True), (1, False)])
        self.assertEqual(braid_3.inverse().crossings, [(3, False), (1, True), (2, False)])

if __name__ == "__main__":
    unittest.main()
