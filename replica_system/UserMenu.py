from lib.Admin import Admin
from lib.Bank import Bank
from lib.Loan import Loan
from lib.Transaction import Transaction
from lib.User import User


def UserMenu(user_instance: User):

    option = -1
    keepRunning = True
    rememberLastSession = False

    while keepRunning:
        print("\nUser Menu")
        print("-------------------")
        print("1. Create a new account")
        print("2. Deposit Cash")
        print("3. Check Available Balance")
        print("4. Check Transction History")
        print("5. Issue a Loan")
        print("6. Money Transfer")
        print("7. Exit")
        print("\n\n-------------------")

        option = int(input("Choose an action: "))
        print()

        match option:
            case 1:
                pass
            case 2:
                try:
                    amount = float(input("Enter amount for deposit: "))
                    user_instance.increase_balance(amount)
                    Transaction(user_instance, user_instance, amount, self_deposit=True)
                except Exception as e:
                    print(e)
            case 3:
                user_instance.check_balance()
            case 4:
                user_instance.check_transaction_history()
            case 5:
                amount = -1
                try:
                    amount = float(input("Enter amount: "))
                except:
                    print("Provide valid amount")
                try:
                    print("Issuing a Loan")
                    Loan(user_instance, amount)
                except Exception as e:
                    print(e)
            case 6:
                user_num = -1
                try:
                    user_num = int(input("Enter receiver id/account_no: "))
                except:
                    print("Enter numeric value only")
                    continue

                if Bank.isNumberAndPositive(user_num) is False:
                    print("Enter numeric value only")
                    continue

                if user_num == user_instance.get_id():
                    print("You can't send money to yourself")
                    continue

                amount = -1

                try:
                    amount = int(input("Enter amount: "))
                except:
                    print("Enter valid amount")
                    continue

                isAdmin = input("Is receiver admin ? (y/N) : ")

                if isAdmin.lower() == "y":
                    try:
                        found_instance = Admin.get_admin_instance(user_num)
                        if found_instance is not None and Bank.isNumberAndPositive(
                            amount
                        ):
                            Transaction(user_instance, found_instance, amount)
                    except Exception as e:
                        print(e)
                else:
                    try:
                        found_instance = User.get_user_instance(user_num)
                        if found_instance is not None and Bank.isNumberAndPositive(
                            amount
                        ):
                            Transaction(user_instance, found_instance, amount)
                    except Exception as e:
                        print(e)
            case 7:
                print("Exiting User Menu")
                keepRunning = False
