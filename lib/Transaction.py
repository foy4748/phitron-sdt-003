from typing import Union
from lib.Admin import Admin
from lib.Bank import Bank
from lib.User import User
from datetime import datetime


class Transaction:
    def __init__(
        self, from_user: Union[User, Admin], to_user: Union[User, Admin], amount
    ) -> None:
        if Bank.isNumberAndPositive(amount):
            isWithDrawOK = from_user.withdraw_balance(amount)
            if isWithDrawOK is True:
                to_user.increase_balance(amount)
                self.from_user = from_user
                self.to_user = to_user
                self.amount = amount
                self.time = datetime.now()
            else:
                # print("Transaction Failed due to Insufficent balance")
                # self.__del__("Transaction Failed due to Insufficent balance")
                raise Exception("Transaction Failed due to Insufficent balance")
        else:
            raise Exception("Transaction Failed due to invalid amount input")
