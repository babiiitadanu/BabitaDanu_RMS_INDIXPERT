from app.dashboard.restaurant_menu import RestaurantMenu
from app.domain.read_write_json import json_methods
SKY_BLUE = "\033[38;5;117m"
RED = "\033[91m"
RESET = "\033[0m"


class FoodOrder:
    def __init__(self): 
        self.file = r"app\database\menu.json" 
        menu = json_methods() 
        self.menu = menu.read_json(self.file) 
        self.order = {}


    def order_food(self):
        category = input("Enter Category (VEG/NON-VEG): ").upper()
        meal_time = input("Enter Meal Time (BREAKFAST/LUNCH/DINNER/DESSERTS): ").upper()
        item = input("Enter Item Name: ")

        try:
            price = int(self.menu[category][meal_time][item])
            qty = int(input("Enter Quantity: "))

            if item in self.order:
                self.order[item]['qty'] += qty
            else:
                self.order[item] = {'price': price, 'qty': qty}

            print(RED +f"{item} added to order"+ RESET)

        except KeyError:
            print(RED+"Item not found in menu!"+RESET)
        except ValueError:
            print("Invalid quantity!")

    def cancel_item(self):
        item = input("Enter item to cancel: ")
        if item in self.order:
            del self.order[item]
            print(f"{item} removed")
        else:
            print("Item not found!")

    
    def run(self):
        while True:
            print(SKY_BLUE+"\n<> FOOD ORDER MENU <>"+RESET)
            print("1. Order Food")
            print("2. Cancel Item")
            print("3. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.order_food()
            elif choice == "2":
                self.cancel_item()
            
            elif choice == "3":
                print("Exiting Food Order...")
                break
            else:
                print(" Invalid choice, try again!")