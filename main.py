# from lib.BaseUser import BaseUser
from lib.Admin import Admin
from lib.Bank import Bank
from lib.Loan import Loan
from lib.Transaction import Transaction
from lib.User import User

admin1 = Admin("Faisal", "faisal.rahman.4748.ph@gmail.com", "Rangpur, Bangladesh", 0)
admin2 = Admin("Faisal", "faisal.rahman.4748.ph.2@gmail.com", "Rangpur, Bangladesh", 1)

user1 = User("Faisal", "faisaljfcl@gmail.com", "Rangpur, Bangladesh", 1)
user2 = User("Faisal", "faisaljfcl02@gmail.com", "Rangpur, Bangladesh", 0)

user1.increase_balance(5000)
user2.increase_balance(2000)
print("Before loan")
user1.check_balance()

Loan(user1, 2000)
Loan(user1, 3000)

Loan(user2, 5000)
Loan(user2, 12000)

print("Performing Transaction")
print("User1 Balance")
user1.check_balance()
print("User2 Balance")
user2.check_balance()
Transaction(user1, user2, 10001)

print("User1 Balance")
user1.check_balance()
print("User2 Balance")
user2.check_balance()
