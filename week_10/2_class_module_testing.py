import unittest
from x_university import Unit

class TestingUnitClass(unittest.TestCase):

    def test_units(self):
        self.specific_testing_on_unit("Name", "Code", 100, 100)
        self.specific_testing_on_unit("Name", "Code", 1, 100)
        self.specific_testing_on_unit("Name", "Code", 30, 100)
        self.specific_testing_on_unit("Name", "Code", -50, 100)
        self.specific_testing_on_unit("Name", "Code", 10, -100)
        self.specific_testing_on_unit("Name", "Code", 0, -5)
        self.specific_testing_on_unit("Name", "Code", 0, 0)
    
    # Notice this doesn't start with test_
    def specific_testing_on_unit(self, name, code, length_weeks, credit_points):
        random_unit: Unit = Unit(name, code, length_weeks, credit_points)
        self.assertEqual(random_unit.get_name(), name)
        self.assertEqual(random_unit.get_code(), code.lower())

        if length_weeks < 0:
            self.assertEqual(random_unit.get_length_weeks(), 0)
        else:
            self.assertEqual(random_unit.get_length_weeks(), length_weeks)
        
        if credit_points < 0:
            self.assertEqual(random_unit.get_credit_points(), 0)
        else:
            self.assertEqual(random_unit.get_credit_points(), credit_points)

if __name__ == "__main__":
    unittest.main()