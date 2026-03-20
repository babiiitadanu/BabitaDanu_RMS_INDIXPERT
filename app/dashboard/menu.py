from app.dashboard.restaurant_menu import RestaurantMenu

YELLOW = "\033[93m"
SKY_BLUE = "\033[38;5;117m"
RESET = "\033[0m"

class ChoiceAdmin:
    def show_menu_admin(self):

        while True:
            print("")
            print(SKY_BLUE+"ADMIN MENU"+RESET)
            print(SKY_BLUE+"1."+RESET ,"VIEW FOOD MENU ")
            print(SKY_BLUE+"2."+RESET ,"UPDATE FOOD ITEM ")
            print(SKY_BLUE+"3."+RESET ,"DELETE FOOD ITEM")
            print(SKY_BLUE+"4."+RESET ,"DELETE STAFF")
            print(SKY_BLUE+"5."+RESET ,"EXIT")

            choice = input(YELLOW+"ENTER YOUR CHOICE :"+RESET)

            if choice == "1":
             object=RestaurantMenu()
             object.show_menu()
             
            elif choice == "2":
             print("Done")
            
            elif choice == "3":
               print("Done")

            elif choice == "4":
                print("Done")

            elif choice == "5":
              break
          
            else:
                print("INVALID CHOICE!")


 
class ChoiceStaff:
    def show_menu_staff(self):

        while True:
            print("")
            print(SKY_BLUE+"STAFF MENU"+RESET)
            print(SKY_BLUE+"1."+RESET ,"VIEW FOOD MENU ")
            print(SKY_BLUE+"2."+RESET ,"TAKE ORDER")
            print(SKY_BLUE+"3."+RESET ,"TABLE BOOKING" )
            print(SKY_BLUE+"4."+RESET ,"GENERATE BILL ")
            print(SKY_BLUE+"5."+RESET ,"EXIT")

            choice = input(YELLOW+"ENTER YOUR CHOICE:"+RESET)

            if choice =="1":
             print("Done")
             
            elif choice == "2":
             print("Done")

            elif choice == "3":
             print("Done")
             
            elif choice == "4":
             print("Done")

            elif choice == "5":
             break
             
            else:
                print("INVALID CHOICE! ")
                
