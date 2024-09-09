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
                amount = int(input("Enter amount for deposit: "))
                try:
                    user_instance.increase_balance(amount)
                except Exception as e:
                    print(e)
            case 3:
                user_instance.check_balance()
            case 4:
                user_instance.check_transaction_history()
            case 5:
                pass
            case 7:
                print("Exiting User Menu")
                keepRunning = False
