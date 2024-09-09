from lib.Bank import Bank
from lib.BaseUser import BaseUser
from lib.User import User


class Admin(BaseUser):
    __admins = []

    def __init__(self, name, email, address, account_type_idx) -> None:
        id = len(self.__admins) + 1
        super().__init__(
            name, email, address, BaseUser._account_types[account_type_idx], id
        )
        self.__admins.append(self)

    def __repr__(self) -> str:
        return f"{self.get_id()} | {super().__repr__()}"

    # Task 3 - Can see all user accounts list
    def view_user_list(self):
        for user in User._users:
            print(user)

    def view_admin_list(self):
        for user in self.__admins:
            print(user)

    # Task 4 - Can check the total available balance of the bank.
    def check_total_bank_balance(self):
        Bank.check_bank_balance()

    # Task 5 - Can check the total loan amount.
    def check_total_loan_amount(self):
        Bank.check_loan_amount()

    # Task 6 - Can on or off the loan feature of the bank.
    def toggle_loan_feature(self):
        Bank._toggle_loan_feature()
