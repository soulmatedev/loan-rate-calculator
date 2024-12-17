from loan_calculator import LoanCalculator

def get_input():
    try:
        loan_amount = float(input("Введите сумму кредита: "))
        loan_term = int(input("Введите срок кредита (в днях): "))

        calculator = LoanCalculator(loan_amount, loan_term)
        rate = calculator.calculate_rate()

        print(f"Ваша процентная ставка по кредиту: {rate}%")

    except ValueError as e:
        print(f"Ошибка ввода: {e}")


if __name__ == "__main__":
    get_input()