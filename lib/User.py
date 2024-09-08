from lib.Bank import Bank
from lib.BaseUser import BaseUser


class User(BaseUser):
    _users = []

    def __init__(self, name, email, address, account_type_idx) -> None:
        super().__init__(
            name, email, address, BaseUser._account_types[account_type_idx]
        )
        self._loans = []
        self.__id = len(self._users) + 1
        self._users.append(self)

    def __repr__(self) -> str:
        Bank._increase_total_loan_amount(50)
        return f"{self.__id} | {super().__repr__()}"
