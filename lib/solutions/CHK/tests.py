import unittest

from checkout_solution import checkout

class TestCheckout(unittest.TestCase):
    def test_checkout_with_valid_input(self):
        inputs_and_outputs = [
            ("AAABBBCCCDDDEE", 360),
            ("A", 50),
            ("ABCD", 115),
            ("AAAAAAABB", 355)
        ]

        for case in inputs_and_outputs:
            self.assertEqual(checkout(case[0]), case[1])

    def test_checkout_with_invalid_input(self):
        inputs_and_outputs = [
            ("ABCDE", -1),
            ("abc", -1),
            (26, -1),
            ("", -1)
        ]

        for case in inputs_and_outputs:
            self.assertEqual(checkout(case[0]), case[1])

if __name__ == '__main__':
    unittest.main()
