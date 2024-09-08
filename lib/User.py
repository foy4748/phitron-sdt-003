from lib.BaseUser import BaseUser


class User(BaseUser):
    users = []

    def __init__(self, name, email, address, account_type_idx) -> None:
        super().__init__(name, email, address, BaseUser.account_types[account_type_idx])
        self.loans = []
        self.id = len(self.users) + 1
        self.users.append(self)

    def __repr__(self) -> str:
        return f"{self.id} | {super().__repr__()}"
