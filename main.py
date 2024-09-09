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

user1.increase_balance(4000)
print("Balance")
user1.check_balance()

try:
    user1.increase_balance("4000")
except Exception as e:
    print(e)

print("Bank Capital")
Bank.check_bank_balance()

# print("Turning OFF Loan")
# admin1.toggle_loan_feature()

try:
    Loan(user1, 1000)
    Loan(user1, 2000)
    Loan(user1, 1000)
except Exception as e:
    print(e)

print("Balance")
user1.check_balance()

print("Bank Capital")
Bank.check_bank_balance()

# print("Deleting User account")
# user1.toggle_delete_status()


try:
    Transaction(user1, user2, 4000)
except Exception as e:
    print(e)
print("Balance")
try:
    user1.check_balance()
    user2.check_balance()
except Exception as e:
    print(e)

Bank.check_all_transaction_history()
