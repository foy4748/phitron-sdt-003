from lib.BaseUser import BaseUser


class Admin(BaseUser):
    admins = []

    def __init__(self, name, email, address, account_type_idx) -> None:
        super().__init__(name, email, address, BaseUser.account_types[account_type_idx])
        self.admins.append(self)
