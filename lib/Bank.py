from abc import ABC


class Bank(ABC):
    __total_bank_balance = 0
    __total_loan_amount = 0
    __total_issued_loans = dict()
    __isLoanFeatureOn = True
    __total_transaction_history = []

    # Balance releated
    @classmethod
    def check_bank_balance(cls):
        print(cls.__total_bank_balance)

    @classmethod
    def _increase_total_bank_balance(cls, amount):
        if cls.isNumberAndPositive(amount) is True:
            cls.__total_bank_balance += amount
        else:
            print("Enter valid number. Balance is Unchanged")
        return cls.__total_bank_balance

    @classmethod
    def _decrease_total_bank_balance(cls, amount):
        if cls.isNumberAndPositive(amount) is True:
            cls.__total_bank_balance -= amount
        else:
            print("Enter valid number. Balance is Unchanged")
        return cls.__total_bank_balance

    # Loan related
    @classmethod
    def check_loan_amount(cls):
        print(cls.__total_loan_amount)

    @classmethod
    def check_issued_loans(cls):
        for _, k in enumerate(cls.__total_issued_loans):
            print(k, cls.__total_issued_loans[k])

    @classmethod
    def _increase_total_loan_amount(cls, amount):
        if cls.isNumberAndPositive(amount) is True:
            cls.__total_loan_amount += amount
        else:
            print("Enter valid number. Loan Amount is Unchanged")
        return cls.__total_loan_amount

    @classmethod
    def _decrease_total_loan_amount(cls, amount):
        if cls.isNumberAndPositive(amount) is True:
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

    @classmethod
    def _append_new_loan(cls, loan):
        temp = cls.__total_issued_loans.get(loan.user.get_id(), [])
        temp.append(loan)
        cls.__total_issued_loans[loan.user.get_id()] = temp

    # Transaction related
    @classmethod
    def record_transaction(cls, transaction):
        cls.__total_transaction_history.append(transaction)

    # Static / Utility Functions
    @staticmethod
    def isNumberAndPositive(num):
        return isinstance(num, (int, float)) and num > 0
