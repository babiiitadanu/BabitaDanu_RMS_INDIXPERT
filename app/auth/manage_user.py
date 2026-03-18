from app.auth.signup import UserSignup
from app.auth.login import Login

YELLOW = "\033[93m"
SKY_BLUE = "\033[38;5;117m"
RESET = "\033[0m"

class Manage():
    def rms_management(self):
        while True:
            print(YELLOW+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"+RESET)
            print(YELLOW+"    THE AROMA ROOFTOP RESTAURANT   "+RESET)
            print(YELLOW+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"+RESET)
            print(SKY_BLUE+"REGISTRATION"+RESET)
            print(SKY_BLUE+"1.SIGNUP"+RESET)
            print(SKY_BLUE+"2.LOGIN"+RESET)
            print(SKY_BLUE+"3.EXIT"+RESET)
               
            print("")
            choice = input("PLEASE ENTER CHOICE: ")                        

            if choice == "1":
                ob = UserSignup()
                ob.dashboard()
            elif choice == "2":
                ob=Login()
                ob.identify_user()
            elif choice == "3":
                print("EXITING..")
                break
            else:
                print("INVALID CHOICE!")

