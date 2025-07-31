import unittest
import copy
from src.mirrormirror import mirrormirror  

class TestMain(unittest.TestCase):

    def test_mirrormirror(self):
        """
        Tests the `mirrormirror` function with various types of inputs to ensure correct behavior.
        
        The test cases include:
        - Comparing identical integers, strings, lists, and dictionaries.
        - Comparing nested lists and their shallow and deep copies.
        
        Each test asserts that the output of `mirrormirror` is `[True, True, True, True]` for inputs that are expected to be equivalent.
        """
        # Base tests
        self.assertEqual(mirrormirror(42, 42), [True, True, True, True])
        self.assertEqual(mirrormirror("hello", "hello"), [True, True, True, True])
        # list,set and dict are not the same object, but have the same content
        self.assertEqual(mirrormirror([1, 2, 3], [1, 2, 3]), [True, False, True, True])
        self.assertEqual(mirrormirror({"key": "value"}, {"key": "value"}), [True, False, True, True])
        self.assertEqual(mirrormirror({1,2,3}, {1,2,3}), [True, False, True, True])
        # sets are unordered, so the order of elements does not matter
        self.assertEqual(mirrormirror({1,2,3}, {1,3,2}), [True, False, True, True])
        # lists are ordered, so the order of elements does matter
        self.assertEqual(mirrormirror([1, 2, 3], [1, 3, 2]), [False, False, True, True])

        #test for nested lists
        x = [[1, 2], [3, 4]]
        y = x[:]
        z = copy.deepcopy(x)
        w = copy.copy(x)
        u = x
        self.assertEqual(mirrormirror(x, y), [True, False, True, True])
        self.assertEqual(mirrormirror(x, z), [True, False, True, True])
        self.assertEqual(mirrormirror(y, z), [True, False, True, True])
        self.assertEqual(mirrormirror(x, w), [True, False, True, True])
        self.assertEqual(mirrormirror(x, u), [True, True, True, True])

        # Different types
        self.assertEqual(mirrormirror(1, "1"), [False, False, False, False])
        self.assertEqual(mirrormirror([1], (1,)), [False, False, False, False])
        self.assertEqual(mirrormirror({"a": 1}, [("a", 1)]), [False, False, False, False])
        self.assertEqual(mirrormirror(1, 1.0), [True, False, False, False])

        # Identity checks
        a = [1, 2]
        b = a
        c = [1, 2]
        self.assertEqual(mirrormirror(a, b), [True, True, True, True])  # same object
        self.assertEqual(mirrormirror(a, c), [True, False, True, True]) # different objects, same value

        # None comparisons
        self.assertEqual(mirrormirror(None, None), [True, True, True, True])
        self.assertEqual(mirrormirror(None, 0), [False, False, False, False])

        # Boolean comparison
        self.assertEqual(mirrormirror(True, True), [True, True, True, True])
        self.assertEqual(mirrormirror(True, False), [False, False, True, True])
        self.assertEqual(mirrormirror(False, False), [True, True, True, True])
        self.assertEqual(mirrormirror([True], [False]), [False, False, True, True])       

if __name__ == '__main__':
    unittest.main()