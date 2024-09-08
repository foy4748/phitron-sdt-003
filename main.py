# from lib.BaseUser import BaseUser
from lib.Admin import Admin
from lib.Bank import Bank
from lib.User import User

admin1 = Admin("Faisal", "faisal.rahman.4748.ph@gmail.com", "Rangpur, Bangladesh", 0)
admin2 = Admin("Faisal", "faisal.rahman.4748.ph.2@gmail.com", "Rangpur, Bangladesh", 1)

user1 = User("Faisal", "faisaljfcl@gmail.com", "Rangpur, Bangladesh", 1)
user2 = User("Faisal", "faisaljfcl02@gmail.com", "Rangpur, Bangladesh", 0)

user1.increase_balance(5000)
user2.increase_balance(2000)
Bank.check_bank_balance()
user1.check_balance()
user2.check_balance()
