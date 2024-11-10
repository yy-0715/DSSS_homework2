import unittest
from math_quiz import get_random_integer, get_random_operater, calculate_expression


class TestMathGame(unittest.TestCase):

    def test_get_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_operater(self):
        # Test if random operator generated are within '+', '-' and '*'
        for _ in range(1000):
             rand_operater = get_random_operater()
             self.assertIn(rand_operater, ['+', '-', '*'])


    def test_calculate_expression(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (10, -3, '*', '10 * -3', -30),
                (-5, -3, '+', '-5 + -3', -8),
                (-8, 2, '-', '-8 - 2', -10)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # Test if the expression and the result is as expected
                expression, result = calculate_expression(num1, num2, operator)
                self.assertEqual(expression, expected_problem)
                self.assertEqual(result, expected_answer)



if __name__ == "__main__":
    unittest.main()
