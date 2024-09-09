from lib.Bank import Bank
from lib.BaseUser import BaseUser


class User(BaseUser):
    _users = []

    def __init__(self, name, email, address, account_type_idx) -> None:
        id = len(self._users) + 1
        super().__init__(
            name, email, address, BaseUser._account_types[account_type_idx], id
        )
        self._loans = []
        self._users.append(self)

    def __repr__(self) -> str:
        return f"{self.get_id()} | {super().__repr__()}"
