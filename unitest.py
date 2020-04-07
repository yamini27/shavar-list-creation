import unittest
import os
from constants import (ALL_TAGS,DEFAULT_DISCONNECT_LIST_CATEGORIES)



class Type_Test_Case(unittest.TestCase):
    def test_type_of_category_filters(self):
        c_f = str
        self.assertEqual(type(category_filters),list)
        with self.assertRaises(ValueError):
            type(category_filters) = c_f


if __name__ == '__main__':
    unittest.main()