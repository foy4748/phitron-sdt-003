from lib.BaseUser import BaseUser


class Admin(BaseUser):
    admins = []

    def __init__(self, name, email, address, account_type_idx) -> None:
        super().__init__(name, email, address, BaseUser.account_types[account_type_idx])
        self.id = len(self.admins) + 1
        self.admins.append(self)

    def __repr__(self) -> str:
        return f"{self.id} | {super().__repr__()}"
