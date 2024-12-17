class LoanCalculator:
    def __init__(self, loan_amount: float, loan_term: int):
        self.loan_amount = loan_amount
        self.loan_term = loan_term
        self.base_rate = self._get_base_rate()

    def _get_base_rate(self) -> float:
        if self.loan_term <= 92:
            return 20.0
        elif 93 <= self.loan_term <= 182:
            return 19.0
        elif 183 <= self.loan_term <= 365:
            return 18.0
        else:
            raise ValueError("Срок кредита не может превышать 365 дней")

    def _adjust_rate_by_amount(self) -> float:
        if self.loan_amount <= 50000:
            return 0.0
        elif 50000 < self.loan_amount <= 100000:
            return -0.5
        else:
            return -1.5

    def calculate_rate(self) -> float:
        adjusted_rate = self.base_rate + self._adjust_rate_by_amount()
        return adjusted_rate