from typing import Union
from lib.Admin import Admin
from lib.Bank import Bank
from lib.User import User
from datetime import datetime


class Transaction:
    def __init__(
        self,
        from_user: Union[User, Admin],
        to_user: Union[User, Admin],
        amount,
        self_deposit=False,
    ) -> None:
        # Logics
        isAmountValid = Bank.isNumberAndPositive(amount)
        isSelfDepositing = self_deposit is True
        isBothUserSame = from_user == to_user

        if isSelfDepositing and isBothUserSame and isAmountValid is True:
            to_user.increase_balance(amount)  # Will also increase bank balance
            self.from_user = from_user
            self.to_user = to_user
            self.amount = amount
            self.self_deposit = self_deposit
            self.time = datetime.now()

            # Recording Transactions
            to_user.perform_transaction(self)
            Bank.record_transaction(self)
            return

        if isAmountValid is True:

            isBankTransferable = Bank.check_transfer_limit(amount)

            if isBankTransferable is False:
                raise Exception("Transaction Failed due to Insufficent CAPITAL")

            isWithDrawOK = None
            try:
                isWithDrawOK = from_user.withdraw_balance(amount)
            except Exception as e:
                print(e)

            if isWithDrawOK is True:
                try:
                    to_user.increase_balance(amount)
                    self.from_user = from_user
                    self.to_user = to_user
                    self.amount = amount
                    self.self_deposit = self_deposit
                    self.time = datetime.now()

                    print(
                        f"Sending...\nFrom: {self.from_user}\nTo: {self.to_user}\nAmount:{self.amount}"
                    )
                    # Recording Transactions
                    to_user.perform_transaction(self)
                    from_user.perform_transaction(self)
                    Bank.record_transaction(self)
                except Exception as e:
                    print(e)
            else:
                # print("Transaction Failed due to Insufficent balance")
                # self.__del__("Transaction Failed due to Insufficent balance")
                raise Exception("Transaction Failed due to Insufficent balance")
        else:
            raise Exception("Transaction Failed due to invalid amount input")

    def __repr__(self) -> str:
        if self.self_deposit:
            return f"Deposite Amount: {self.amount} BDT\nTime: {self.time.strftime('%A, %B %d, %Y %I:%M %p')}"
        else:
            return f"From: {self.from_user}\nTo: {self.to_user}\nAmount: {self.amount} BDT\nTime: {self.time.strftime('%A, %B %d, %Y %I:%M %p')}"
