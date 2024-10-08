from abc import ABC

from lib.Bank import Bank

# Decorators


def check_is_deleted_user(func):
    def wrapper(self, *args, **kwargs):
        if self._isDeleted is False:
            return func(self, *args, **kwargs)
        else:
            raise Exception("User is Deleted")

    return wrapper


class BaseUser(ABC):
    _account_types = ("SAVINGS", "CURRENT")

    def __init__(self, name, email, address, account_type, id, role="USER"):
        self.__name = name
        self.__email = email
        self.__address = address
        self.__account_type = account_type
        self.__balance = 0
        self.__loan_amount = 0
        self.__loans = []
        self.__transactions = []
        self.__id = id
        self._isDeleted = False
        self._role = role

    # @check_is_deleted_user
    def get_id(self):
        return self.__id

    @check_is_deleted_user
    def get_role(self):
        return self._role

    # @check_is_deleted_user
    # Allowing Reactivate the user
    def toggle_delete_status(self):
        if self._isDeleted is False:
            print("Deleting User account")
            self._isDeleted = True
        else:
            print("Re-activating User account")
            self._isDeleted = False

    # @check_is_deleted_user
    def __repr__(self) -> str:
        if self._isDeleted is False:
            return f"{self.__name} || {self.__email} || {self.__address}"
        else:
            return f"(deactivated) || {self.__name} || {self.__email}"

    # Balance releated
    @check_is_deleted_user
    def check_balance(self):
        print(self.__balance)

    @check_is_deleted_user
    def increase_balance(self, amount):
        if Bank.isNumberAndPositive(amount):
            self.__balance += amount
            Bank._increase_total_bank_balance(amount)
        else:
            raise Exception("Enter valid amount for balance increase")

    @check_is_deleted_user
    def withdraw_balance(self, amount):
        if self.__balance < amount:
            raise Exception("Withdrawal amount exceeded")
            # return False

        if Bank.isNumberAndPositive(amount):
            try:
                Bank._decrease_total_bank_balance(amount)
                self.__balance -= amount
            except Exception as e:
                print(e)
                return False
            return True
        else:
            raise Exception("Provide valid amount")

    # Loan related

    @check_is_deleted_user
    def check_loan_amount(self):
        print(self.__loan_amount)

    @check_is_deleted_user
    def issue_a_loan(self, loan):
        if len(self.__loans) < 2:
            self.__loans.append(loan)
            self.__loan_amount += loan.amount
        else:
            raise Exception("Already have issued 2 loans")

    @check_is_deleted_user
    def change_account_type(self, account_type_idx):
        self.__account_type = self._account_types[account_type_idx]
        return self.__account_type

    # Transaction related

    @check_is_deleted_user
    def perform_transaction(self, transaction):
        self.__transactions.append(transaction)

    @check_is_deleted_user
    def check_transaction_history(self):
        print("Transction history")
        print("===================")
        for transaction in reversed(self.__transactions):
            print("\n-----------------")
            print(transaction)
            print("-----------------\n")
        print("===================")
