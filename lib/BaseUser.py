from abc import ABC


class BaseUser(ABC):
    account_types = ("SAVINGS", "CURRENT")

    def __init__(self, name, email, address, account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0

    def __repr__(self) -> str:
        return f"{self.name} || {self.email}"
