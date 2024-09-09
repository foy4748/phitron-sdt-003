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

print("Created Users successfully....")

print("User1 Depositing 4000")
user1.increase_balance(4000)

print("User2 Taking Loan 3000")
Loan(user2, 3000)


print("\n\nChecking Balance\n")
print("User1")
user1.check_balance()
print("User2")
user2.check_balance()
print("\n\nBank\n")
print("Bank Balance")
Bank.check_bank_balance()
print("Bank Loan")
Bank.check_loan_amount()

print("User 2 withdrawing 3000")
user2.withdraw_balance(3000)
print("\nUser2 Balance")
user2.check_balance()

try:
    Transaction(user1, user2, 4000)
except Exception as e:
    print(e)
