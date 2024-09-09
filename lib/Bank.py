from abc import ABC


def check_is_loan_feature_turned_off(func):
    def wrapper(self, *args, **kwargs):
        if self._isLoanFeatureOn is True:
            return func(self, *args, **kwargs)
        else:
            raise Exception("Issuing a Loan is currently unavailable")

    return wrapper


class Bank(ABC):
    __total_bank_balance = 0
    __total_loan_amount = 0
    __total_issued_loans = dict()
    _isLoanFeatureOn = True
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
            if cls.__total_bank_balance >= amount:
                cls.__total_bank_balance -= amount
            else:
                raise Exception("bank is bankrupt")
        else:
            # print("Enter valid number. Balance is Unchanged")
            raise Exception("Enter valid number. Balance is Unchanged")
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
    @check_is_loan_feature_turned_off
    def _increase_total_loan_amount(cls, amount):
        if cls.isNumberAndPositive(amount) is True:
            cls.__total_loan_amount += amount
        else:
            print("Enter valid number. Loan Amount is Unchanged")
        return cls.__total_loan_amount

    @classmethod
    # Allowing loan resolve
    def _decrease_total_loan_amount(cls, amount):  # Due to loan resolve
        if cls.isNumberAndPositive(amount) is True:
            cls.__total_loan_amount -= amount
        else:
            print("Enter valid number. Loan Amount is Unchanged")
        return cls.__total_loan_amount

    @classmethod
    @check_is_loan_feature_turned_off
    def _append_new_loan(cls, loan):
        temp = cls.__total_issued_loans.get(loan.user.get_id(), [])
        temp.append(loan)
        cls.__total_issued_loans[loan.user.get_id()] = temp

    @classmethod
    def _toggle_loan_feature(cls):
        if cls._isLoanFeatureOn is True:
            cls._isLoanFeatureOn = False
        else:
            cls.isLoanFeatureOn = True
        return cls._isLoanFeatureOn

    # Transaction related
    @classmethod
    def record_transaction(cls, transaction):
        cls.__total_transaction_history.append(transaction)

    @classmethod
    def check_all_transaction_history(cls):
        print("Transction history")
        print("===================")
        for transaction in cls.__total_transaction_history:
            print("-----------------")
            print(transaction)
            print("-----------------")
        print("===================")

    # Static / Utility Functions
    @staticmethod
    def isNumberAndPositive(num):
        return isinstance(num, (int, float)) and num > 0
