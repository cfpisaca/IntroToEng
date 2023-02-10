import unittest
from labs import lab3


class MyTestCase(unittest.TestCase):
    def test_add_dashes(self):
        result = lab3.add_dashes("hi")
        self.assertEqual("-hi-", result)
        result = lab3.add_dashes("asdf")
        self.assertEqual("-asdf-", result)

    def test_reverse_order(self):
        result = lab3.reverse_order("apple", "banana")
        self.assertEqual("bananaapple", result)
        result = lab3.reverse_order("yo", "hey")
        self.assertEqual("heyyo", result)

    def test_print2_return1(self):
        result = lab3.print2_return1("apple", "banana", "coconut")
        self.assertEqual("banana", result)
        result = lab3.print2_return1("one", "two", "three")
        self.assertEqual("two", result)

if __name__ == '__main__':
    unittest.main()