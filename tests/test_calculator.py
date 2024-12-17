import unittest
from loan_calculator import LoanCalculator

class TestLoanCalculator(unittest.TestCase):

    def test_base_rate(self):
        calc = LoanCalculator(40000, 100)
        self.assertEqual(calc._get_base_rate(), 19.0)

    def test_adjusted_rate(self):
        calc_1 = LoanCalculator(45000, 100)
        calc_2 = LoanCalculator(60000, 100)
        calc_3 = LoanCalculator(150000, 100)

        self.assertEqual(calc_1._adjust_rate_by_amount(), 0.0)
        self.assertEqual(calc_2._adjust_rate_by_amount(), -0.5)
        self.assertEqual(calc_3._adjust_rate_by_amount(), -1.5)

    def test_final_rate(self):
        calc = LoanCalculator(60000, 100)
        self.assertEqual(calc.calculate_rate(), 18.5)

if __name__ == "__main__":
    unittest.main()
