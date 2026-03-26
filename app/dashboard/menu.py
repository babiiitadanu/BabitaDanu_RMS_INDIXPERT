from app.dashboard.restaurant_menu import RestaurantMenu
from app.order.orderrestaurant import FoodOrder
from app.dashboard.dlt_staff import StaffManager
from app.booking.table_book import TableBookingSystem
from app.bill.billing import RestaurantBill


YELLOW = "\033[93m"
SKY_BLUE = "\033[38;5;117m"
RESET = "\033[0m"

class ChoiceAdmin:
    def show_menu_admin(self):

        while True:
            
            print(SKY_BLUE+"\n<> ADMIN MENU <>"+RESET)
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
             object1=RestaurantMenu()
             object1.update_menu()
            
            elif choice == "3":
             object2=RestaurantMenu()
             object2.delete_item()
         
            elif choice == "4":
             object3 = StaffManager()
             object3.remove_users()
               
            elif choice == "5":
              break
          
            else:
                print("INVALID CHOICE!")


 
class ChoiceStaff:
    def show_menu_staff(self):

        while True:
           
            print(SKY_BLUE+"\n<> STAFF MENU <>"+RESET)
            print(SKY_BLUE+"1."+RESET ,"VIEW FOOD MENU ")
            print(SKY_BLUE+"2."+RESET ,"TAKE ORDER")
            print(SKY_BLUE+"3."+RESET ,"TABLE BOOKING" )
            print(SKY_BLUE+"4."+RESET ,"GENERATE BILL ")
            print(SKY_BLUE+"5."+RESET ,"EXIT")

            choice = input(YELLOW+"ENTER YOUR CHOICE:"+RESET)

            if choice =="1":
             object=RestaurantMenu()
             object.show_menu()
             
            elif choice == "2":
             object1= FoodOrder()
             object1.run()

            elif choice == "3":
             object2 = TableBookingSystem()
             object2.run()

            elif choice == "4":
             object2 =RestaurantBill()
             object2.generate_bill()

            elif choice == "5":
             break
             
            else:
                print("INVALID CHOICE! ")
                