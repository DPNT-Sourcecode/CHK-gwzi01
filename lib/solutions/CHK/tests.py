import unittest

from checkout_solution import checkout

class TestCheckout(unittest.TestCase):
    def test_checkout_with_valid_input(self):
        inputs_and_outputs = [
            ("AAABBBCCCDDD", 310),
            ("A", 50),
            ("ABCD", )
        ]

        for case in inputs_and_outputs:
            self.assertEqual(hello(case[0]), case[1])

    def test_non_string_raises_error(self):
        with self.assertRaises(Exception) as context:
            hello(2)

        self.assertTrue("A string must be passed to this function" in str(context.exception))

if __name__ == '__main__':
    unittest.main()