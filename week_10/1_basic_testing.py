import unittest

"""
Inheritence is not taught in this unit
However the basic idea is that when a class inherets from another class
this means that it has all it's methods and attributes
The child class can then add more methods and attributes

As an example, imagine you had a class which represented an object in a game
call this class GameComponent
Every single GameComponent has an image and position. 
You can create a new class PlayableCharacter which inherets from GameComponent
Every PlayableCharacter is a GameComponent (has an image and a position)
But you might want to add more code to PlayableCharacter which makes them playable.

We are doing something similar with the class unittest.TestCase
However unittest.TestCase is special because it has some extra funtionality. 
"""

class TestStringMethods(unittest.TestCase):
    # Each method is a different test
    # The test it run automatically if it states with the word test_
    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()