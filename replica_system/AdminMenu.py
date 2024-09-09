from lib.Admin import Admin


def AdminMenu(admin_instance: Admin):
    option = -1
    keepRunning = True

    while keepRunning:
        print("\n\nAdmin Menu")
        print("-------------------")
        print("1. Create a new admin account")
        print("2. Delete an account")
        print("3. View all user accounts list")
        print("4. Check the Total Available Balance of The Bank")
        print("5. Check the Total Loan Amount")
        print("6. Toggle ON/OFF providing Loan")
        print("7. Exit Menu")
        print("\n\n-------------------")

        option = int(input("Choose an action: "))
        print()

        match option:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                admin_instance.toggle_loan_feature()
            case 7:
                print("Exiting Admin Menu")
                keepRunning = False
