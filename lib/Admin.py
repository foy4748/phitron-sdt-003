from lib.BaseUser import BaseUser


class Admin(BaseUser):
    __admins = []

    def __init__(self, name, email, address, account_type_idx) -> None:
        super().__init__(
            name, email, address, BaseUser._account_types[account_type_idx]
        )
        self.__id = len(self.__admins) + 1
        self.__admins.append(self)

    def __repr__(self) -> str:
        return f"{self.__id} | {super().__repr__()}"
