import unittest

def reciprocate(x: float) -> float:
    if x == 0:
        raise ValueError("Cannot divide by 0")
    return 1 / x

class TestFunc(unittest.TestCase):

    def test_reciprocate(self):
        # self.assertEqual(reciprocate(0), float("inf"))
        self.assertRaises(ValueError, reciprocate, 0) # Higher Order function

if __name__ == "__main__":
    unittest.main()
