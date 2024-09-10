from lib.Bank import Bank
from lib.BaseUser import BaseUser
from lib.User import User


class Admin(BaseUser):
    __admins = []

    def __init__(
        self, name: str, email: str, address: str, account_type_idx: int
    ) -> None:
        id = len(self.__admins) + 1
        super().__init__(
            name, email, address, BaseUser._account_types[account_type_idx], id, "ADMIN"
        )
        self.__admins.append(self)

    def __repr__(self) -> str:
        return f"{self.get_id()} | {super().__repr__()}"

    @classmethod
    def get_admin_instance(cls, num):
        idx = num - 1
        admin_instance = None
        try:
            admin_instance = cls.__admins[idx]
            return admin_instance
        except:
            print(f"User not found for id/account_no {num}")
            return admin_instance

    # Task 2 - Can delete any user account
    def delete_a_user(self, num):
        User._delete_a_user(num)

    @classmethod
    def _delete_an_admin(cls, num):
        idx = num - 1
        to_be_deleted = cls.__admins[idx]
        to_be_deleted.toggle_delete_status()

    # Task 3 - Can see all user accounts list
    def view_user_list(self):
        User.view_user_list()

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
