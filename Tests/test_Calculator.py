import unittest

from Calculator.Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_calculator_addition(self):
        calculator = Calculator()
        result = calculator.addition(1, 2)
        self.assertEqual(3, result)

    def test_calculator_subtraction(self):
        calculator = Calculator()
        result = calculator.subtraction(1, 2)
        self.assertEqual(-1, result)

    def test_calculator_multiplication(self):
        calculator = Calculator()
        result = calculator.multiplication(2, 2)
        self.assertEquals(4, result)

    def test_calculator_division(self):
        calculator = Calculator()
        result= calculator.divison(2,2)
        self.assertEqual(1,result)

    def test_calculator_squareRoot(self):
        calculator = Calculator()
        result = calculator.square_root(9)
        self.assertEqual(3,result)

    def test_calculator_square (self):
        calculator = Calculator()
        result = calculator.square(2)
        self.assertEqual(4,result)



if __name__ == '__main__':
    unittest.main()
