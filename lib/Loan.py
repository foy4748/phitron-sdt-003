from typing import Union
from lib.Admin import Admin
from lib.Bank import Bank
from lib.User import User


class Loan:
    def __init__(self, user: Union[User, Admin], amount) -> None:
        self.user = user
        if Bank.isNumberAndPositive(amount):
            self.amount = amount

            try:
                Bank._decrease_total_bank_balance(amount)
                Bank._increase_total_loan_amount(amount)
            except Exception as e:
                print(e)
                return

            try:
                user.increase_balance(amount)
                user.issue_a_loan(self)
                Bank._append_new_loan(self)
            except Exception as e:
                print(e)
        else:
            raise Exception("Can't issue loan using invalid amount")
