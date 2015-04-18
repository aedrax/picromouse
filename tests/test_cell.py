import unittest

class TestCellMethods(unittest.TestCase):
    def test_get_weight(self):
        # Make sure a newly-initialized Cell object
        # has the appropriate weight value.
        c = Cell()
        self.assertEqual(c.get_weight(), 0)
        # Make sure that an updated weight value for a Cell
        # object is reflected in the get_weight() method.
        some_integer = randint(0, 15)
        c.weight = some_integer
        self.assertEqual(c.get_weight(), some_integer)

    def test_get_coordinates(self):
        return 0