import unittest

from checkout_solution import checkout

class TestCheckout(unittest.TestCase):
    def test_checkout_with_valid_input(self):
        inputs_and_outputs = [
            ("AAABBBCCCDDDEE", 360),
            ("A", 50),
            ("AAA", 130),
            ("AAAAA", 200),
            ("AAAAAA", 250),
            ("BBEEEE", 160),
            ("ABCDE", 155),
            ("AAAAAAABB", 345),
            ("EE", 80)
            ("AAABBBCCCDDDEEFF", 380),
            ("AAABBBCCCDDDEEFFF", 380),
            ("FFFF", 30),
            ("FFFFFF", 40)
        ]

        for case in inputs_and_outputs:
            self.assertEqual(checkout(case[0]), case[1])

    def test_checkout_with_invalid_input(self):
        inputs_and_outputs = [
            ("ABCDX", -1),
            ("abc", -1),
            (26, -1),
        ]

        for case in inputs_and_outputs:
            self.assertEqual(checkout(case[0]), case[1])

if __name__ == '__main__':
    unittest.main()


