import unittest
import Calculator


class MyTestCase(unittest.TestCase):

    def test_addition(self):
        assert 4 == Calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == Calculator.subtract(4, 2)


if __name__ == '__main__':
    unittest.main()
