from abc import ABC


class Bank(ABC):
    __total_bank_balance = 0
    __total_loan_amount = 0
    __isLoanFeatureOn = True

    @classmethod
    def check_bank_balance(cls):
        print(cls.__total_bank_balance)

    @classmethod
    def _increase_total_bank_balance(cls, amount):
        if Bank.isNumberAndPositive(amount) is True:
            cls.__total_bank_balance += amount
        else:
            print("Enter valid number. Balance is Unchanged")
        return cls.__total_bank_balance

    @classmethod
    def _decrease_total_bank_balance(cls, amount):
        if Bank.isNumberAndPositive(amount) is True:
            cls.__total_bank_balance -= amount
        else:
            print("Enter valid number. Balance is Unchanged")
        return cls.__total_bank_balance

    @classmethod
    def _increase_total_loan_amount(cls, amount):
        if Bank.isNumberAndPositive(amount) is True:
            cls.__total_loan_amount += amount
        else:
            print("Enter valid number. Loan Amount is Unchanged")
        return cls.__total_loan_amount

    @classmethod
    def _decrease_total_loan_amount(cls, amount):
        if Bank.isNumberAndPositive(amount) is True:
            cls.__total_loan_amount -= amount
        else:
            print("Enter valid number. Loan Amount is Unchanged")
        return cls.__total_loan_amount

    @classmethod
    def _toggle_loan_feature(cls):
        if cls.__isLoanFeatureOn is True:
            cls.__isLoanFeatureOn = False
        else:
            cls.isLoanFeatureOn = True
        return cls.__isLoanFeatureOn

    @staticmethod
    def isNumberAndPositive(num):
        return isinstance(num, (int, float)) and num > 0
