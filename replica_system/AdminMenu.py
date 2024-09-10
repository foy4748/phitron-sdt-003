from lib.Admin import Admin
from lib.BaseUser import BaseUser


def AdminMenu(admin_instance: Admin):
    option = -1
    keepRunning = True
    # rememberLastSession = False

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
                print("Select Account Type")
                print("-------------------")
                account_type_num = -1
                for idx, account_type in enumerate(BaseUser._account_types):
                    print(str(idx + 1) + ".", account_type)
                try:
                    account_type_num = int(input("Enter Type no. : "))
                except:
                    print("Enter valid no.")
                    continue

                name = input("Enter name: ")
                email = input("Enter email: ")
                address = input("Enter address: ")

                try:
                    Admin(name, email, address, account_type_num - 1)
                    print("Successfully created Admin account")
                except:
                    print("Admin account creation FAILED")
                    continue
            case 2:
                print("Select User Type")
                print("1. Normal User")
                print("2. Admin User")
                user_type = int(input("Choose an action: "))
                print("\n")
                if user_type == 1:
                    admin_instance.view_user_list()
                    user_id = int(input("Enter User number: "))
                    admin_instance.delete_a_user(user_id)
                if user_type == 2:
                    admin_instance.view_admin_list()
                    user_id = int(input("Enter User number: "))
                    Admin._delete_an_admin(user_id)
                else:
                    print("Provide a valid option")
            case 3:
                print("Select User Type")
                print("1. Normal User")
                print("2. Admin User")
                user_type = int(input("Choose an action: "))
                if user_type == 1:
                    admin_instance.view_user_list()
                if user_type == 2:
                    admin_instance.view_admin_list()
                else:
                    print("Provide a valid option")
            case 4:
                admin_instance.check_total_bank_balance()
            case 5:
                admin_instance.check_total_loan_amount()
            case 6:
                admin_instance.toggle_loan_feature()
            case 7:
                print("Exiting Admin Menu")
                keepRunning = False
