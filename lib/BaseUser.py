from abc import ABC

from lib.Bank import Bank


class BaseUser(ABC):
    _account_types = ("SAVINGS", "CURRENT")

    def __init__(self, name, email, address, account_type):
        self.__name = name
        self.__email = email
        self.__address = address
        self.__account_type = account_type
        self.__balance = 0
        # self.__loan = 0

    def __repr__(self) -> str:
        return f"{self.__name} || {self.__email} || {self.__address}"

    # Balance releated
    def check_balance(self):
        print(self.__balance)

    def increase_balance(self, amount):
        if Bank.isNumberAndPositive(amount):
            self.__balance += amount
            Bank._increase_total_bank_balance(amount)

    def withdraw_balance(self, amount):
        if Bank.isNumberAndPositive(amount):
            self.__balance -= amount
            Bank._decrease_total_bank_balance(amount)

    def change_account_type(self, account_type_idx):
        self.__account_type = self._account_types[account_type_idx]
        return self.__account_type
