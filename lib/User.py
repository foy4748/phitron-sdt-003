from lib.BaseUser import BaseUser


class User(BaseUser):
    __users = []

    def __init__(self, name, email, address, account_type_idx) -> None:
        id = len(self.__users) + 1
        super().__init__(
            name, email, address, BaseUser._account_types[account_type_idx], id
        )
        self._loans = []
        self.__users.append(self)

    @classmethod
    def _delete_a_user(cls, num):
        idx = num - 1
        to_be_deleted = cls.__users[idx]
        to_be_deleted.toggle_delete_status()

    @classmethod
    def view_user_list(cls):
        for user in cls.__users:
            print(user)

    def __repr__(self) -> str:
        return f"{self.get_id()} | {super().__repr__()}"
