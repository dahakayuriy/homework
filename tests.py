import unittest


# def sum(a, b):
#     return a + b


# def is_even(number):
#     return number % 2 == 0


# class TestSumFunction(unittest.TestCase):

#     def test_positive_numbers(self):
#         result = sum(2, 2)
#         self.assertEqual(result, 4, "Sum of positive numbers is incorrect")

#     def test_negative_numbers(self):
#         result = sum(-2, -3)
#         self.assertAlmostEqual(
#             result, -5, "Sum of negative numbers is incorrect")

#     def test_mixed_numbers(self):
#         result = sum(2, -3)
#         self.assertEqual(result, -1, "Sum of mixed numbers is incorrect")

#     def test_zero_sum(self):
#         result = sum(0, 0)
#         self.assertEqual(result, 0, "Sum of zeros is incorrect")

#     def test_even_numbers(self):
#         result = is_even(4)
#         self.assertTrue(result, "Function should return True for even numbers")

#     def test_odd_number(self):
#         result = is_even(7)
#         self.assertFalse(
#             result, "Function should return False for odd numbers")

#     def test_negative_even_number(self):
#         result = is_even(-6)
#         self.assertTrue(
#             result, "Function should return True for negative even numbers")

#     def test_zero(self):
#         result = is_even(0)
#         self.assertTrue(result, "Function should return True for zero")


# if __name__ == '__main__':
#     unittest.main()

################################################


# def calculate_tax(income):
#     if income <= 5000:
#         return income * 0.1
#     elif 5001 <= income <= 10000:
#         return income * 0.15
#     else:
#         return income * 0.2


# class TestCalculateTaxFunction(unittest.TestCase):

#     def test_single_tax_rate(self):
#         result = calculate_tax(4000)
#         self.assertEqual(
#             result, 400, "Tax calculation for a single tax rate is incorrect")

#     def test_multiple_tax_rates(self):
#         result = calculate_tax(8000)
#         self.assertEqual(
#             result, 1200, "Tax calculation for multiple tax rates is incorrect")

#     def test_large_income(self):
#         result = calculate_tax(15000)
#         self.assertEqual(
#             result, 3000, "Tax calculation for large income is incorrect")


# if __name__ == '__main__':
#     unittest.main()
##################################################

def calculate_project_cost(base_rate, hours_worked, additional_expenses=0):
    return base_rate * hours_worked + additional_expenses


class TestProjectCostCalculation(unittest.TestCase):
    def test_correct_calculation(self):
        result = calculate_project_cost(base_rate=50, hours_worked=10)
        self.assertEqual(result, 500, "Incorect project cost calculation")

    def test_additional_expenses(self):
        result = calculate_project_cost(
            base_rate=50, hours_worked=10, additional_expenses=100)
        self.assertEqual(
            result, 600, "Incorrect project cost calculation with additional expenses")

    def test_different_hours(self):
        result_1 = calculate_project_cost(base_rate=50, hours_worked=5)
        result_2 = calculate_project_cost(base_rate=50, hours_worked=15)
        self.assertNotEqual(
            result_1, result_2, "Project cost should vary with different hours worked")

    def test_minimum_constrainst(self):
        result = calculate_project_cost(
            base_rate=1, hours_worked=1, additional_expenses=0)
        self.assertEqual(
            result, 1, "Incorrect project cost calculation for minimum constraints")


if __name__ == '__main__':
    unittest.main()
