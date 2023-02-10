import unittest
from labs import lab2


class MyTestCase(unittest.TestCase):
    def test_say_hi(self):
        result = lab2.say_hi()
        self.assertEqual("hi", result)

    def test_say_hi_to_1(self):
        result = lab2.say_hi_to("jane")
        self.assertEqual("hi jane", result)
        result2 = lab2.say_hi_to("James")
        self.assertEqual("hi James", result2)


if __name__ == '__main__':
    unittest.main()