

YELLOW = "\033[93m"
SKY_BLUE = "\033[38;5;117m"
RESET = "\033[0m"

class ChoiceAdmin:
    def show_menu_admin(self):

        while True:
           
            print(SKY_BLUE+"ADMIN MENU"+RESET)
            print("1.VIEW FOOD MENU ")
            print("2.UPDATE FOOD ITEM ")
            print("3.DELETE FOOD ITEM")
            print("4.DELETE STAFF")
            print("5.EXIT")

            choice = input(YELLOW+"ENTER YOUR CHOICE :"+RESET)

            if choice == "1":
               pass
            elif choice == "2":
              pass

            elif choice == "3":
               pass

            elif choice == "4":
                pass

            elif choice == "5":
              break
          
            else:
                print("INVALID CHOICE!")


 
class ChoiceAdmin:
    def show_menu_staff(self):

        while True:
            
            print(SKY_BLUE+"STAFF MENU"+RESET)
            print("1.VIEW FOOD MENU ")
            print("2.TAKE ORDER")
            print("3.TABLE BOOKING" )
            print("4.GENERATE BILL ")
            print("5.EXIT")

            choice = input(YELLOW+"ENTER YOUR CHOICE:"+RESET)

            if choice =="1":
                pass

            elif choice == "2":
                pass

            elif choice == "3":
                pass

            elif choice == "4":
                pass

            else:
                print("INVALID CHOICE! ")
                
