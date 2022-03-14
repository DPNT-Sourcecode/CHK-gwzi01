import unittest

from hello_solution import hello

class TestHelloWorld(unittest.TestCase):
    def test_hello_world_with_string(self):
        inputs_and_outputs = [
            ("John", "Hello World!"),
            ("Dave", "Hello World!"),
        ]

        for case in inputs_and_outputs:
            self.assertEqual(hello(case[0]), case[1])

    def test_non_string_raises_error(self):
        with self.assertRaises(Exception) as context:
            hello(2)

        self.assertTrue("A string must be passed to this function" in str(context.exception))

if __name__ == '__main__':
    unittest.main()
