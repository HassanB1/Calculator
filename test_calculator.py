import unittest
import Calculator as calc


class MyTestCase(unittest.TestCase):

    def test_addition(self):
        assert 4 == calc.Calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calc.Calculator.subtract(4, 2)

    def test_multiply(self):
        assert 4 == calc.Calculator.multiply(2, 2)


if __name__ == '__main__':
    unittest.main()
