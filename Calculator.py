"""
Calculator library containing basic math operations.
"""
import logger as lgr


class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def add(first_term: str, second_term: str):
        lgr.logger('calculator.log', str(first_term) + " " + str(second_term))
        lgr.logger('calculator.log', int(first_term) + int(second_term))
        return first_term + second_term

    @staticmethod
    def subtract(first_term: str, second_term: str):
        lgr.logger('calculator.log', str(first_term) + " " + str(second_term))
        lgr.logger('calculator.log', int(first_term) - int(second_term))
        return first_term - second_term

    @staticmethod
    def multiply(first_term: str, second_term: str):
        lgr.logger('calculator.log', str(first_term) + " " + str(second_term))
        lgr.logger('calculator.log', int(first_term) * int(second_term))
        return first_term * second_term


def main():
    calc = Calculator()
    print(calc.add(5, 6))
    print(calc.subtract(6, 3))
    print(calc.multiply(3, 3))


if __name__ == '__main__':
    main()
