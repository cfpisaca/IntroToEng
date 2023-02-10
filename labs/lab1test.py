import unittest
from labs.lab1 import *


class MyTestCase(unittest.TestCase):
    def test_sayHello(self):
        result = sayHello()
        self.assertEqual("Hello", result)

    def test_sayHiTo(self):
        result = sayHiTo("john")
        self.assertEqual("hi john.", result)
        result = sayHiTo("jane")
        self.assertEqual("hi jane.", result)

    def test_greet(self):
        result = greet("Hello", "Carrie")
        self.assertEqual("Hello Carrie", result)
        result = greet("Yo", "Charlie")
        self.assertEqual("Yo Charlie", result)


if __name__ == '__main__':
    unittest.main()