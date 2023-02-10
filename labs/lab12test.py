import unittest
from labs import lab12


class MyTestCase(unittest.TestCase):
    def test_get_list_of_words(self):
        input = "one two three"
        result = lab12.get_list_of_words(input)
        self.assertListEqual(["one", "two", "three"], result)
        input = "random words of various lengths"
        result = lab12.get_list_of_words(input)
        self.assertListEqual(["random", "words", "of", "various", "lengths"], result)

    def test_make_sentence(self):
        test_data = ["one", "two", "three"]
        result = lab12.make_sentence(test_data)
        self.assertEqual("one two three", result)
        test_data = ["random", "words", "of", "various", "lengths"]
        result = lab12.make_sentence(test_data)
        self.assertEqual("random words of various lengths", result)

    def test_reverse_words(self):
        input = "bob loves alice"
        result = lab12.reverse_words(input)
        self.assertEqual("alice loves bob", result)
        input = "one two three four"
        result = lab12.reverse_words(input)
        self.assertEqual("four three two one", result)

    def test_floor_log_base_2(self):
        result = lab12.floor_log_base_2(2)
        self.assertEqual(1, result)
        result = lab12.floor_log_base_2(3)
        self.assertEqual(1, result)
        for i in range(4, 8):
            result = lab12.floor_log_base_2(i)
            self.assertEqual(2, result)
        for i in range(8, 16):
            result = lab12.floor_log_base_2(i)
            self.assertEqual(3, result)
        for i in range(16, 32):
            result = lab12.floor_log_base_2(i)
            self.assertEqual(4, result)
        #etc etc

    def test_next_vowel(self):
        map_to_a = "avwxyz"
        import random
        index = random.randint(0, len(map_to_a)-1)
        result = lab12.next_vowel(map_to_a[index])
        self.assertEqual("a", result)
        map_to_e = "bcde"
        index = random.randint(0, len(map_to_e)-1)
        result = lab12.next_vowel(map_to_e[index])
        self.assertEqual("e", result)
        map_to_i = "fghi"
        index = random.randint(0, len(map_to_i)-1)
        result = lab12.next_vowel(map_to_i[index])
        self.assertEqual("i", result)
        map_to_o = "jklmno"
        index = random.randint(0, len(map_to_o)-1)
        result = lab12.next_vowel(map_to_o[index])
        self.assertEqual("o", result)
        map_to_u = "pqrstu"
        index = random.randint(0, len(map_to_u)-1)
        result = lab12.next_vowel(map_to_u[index])
        self.assertEqual("u", result)

if __name__ == '__main__':
    unittest.main()