from lib.Admin import Admin
from lib.User import User
from replica_system.AdminMenu import AdminMenu
from replica_system.UserMenu import UserMenu


def StartMenu():
    option = -1
    keepRunning = True
    # rememberLastSession = False

    while keepRunning:
        print("\n\nStart Menu")
        print("-------------------")
        print("1. User Menu")
        print("2. Admin Menu")
        print("3. Exit Menu")
        print("\n\n-------------------")

        option = int(input("Choose an action: "))
        print()

        match option:
            case 1:
                user_num = -1
                try:
                    user_num = int(input("Enter id/account_no: "))
                except:
                    print("Enter numeric value only")
                    continue

                try:
                    user_instance = User.get_user_instance(user_num)
                    if user_instance is not None:
                        UserMenu(user_instance)
                except Exception as e:
                    print(e)
            case 2:
                user_num = -1
                try:
                    user_num = int(input("Enter receiver id/account_no: "))
                except:
                    print("Enter numeric value only")
                    continue

                try:
                    admin_instance = Admin.get_admin_instance(user_num)
                    if admin_instance is not None:
                        AdminMenu(admin_instance)
                except Exception as e:
                    print(e)
            case 3:
                print("Exiting Start Menu")
                keepRunning = False
