from app.dashboard.restaurant_menu import RestaurantMenu
from app.domain.read_write_json import json_methods

SKY_BLUE = "\033[38;5;117m"
RED = "\033[91m"
RESET = "\033[0m"


class FoodOrder:
    def __init__(self):
        self.file = r"app\database\menu.json"
        self.order_file = r"app\database\order.json"

        self.read_write = json_methods()
        self.menu = self.read_write.read_json(self.file)
        self.orderjson = self.read_write.read_json(self.order_file)

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

            print(RED + f"{item} added to order" + RESET)

           
            self.orderjson = [self.order] 
            self.read_write.write_json(self.order_file, self.orderjson)

        except KeyError:
            print(RED + "Item not found in menu!" + RESET)
        except ValueError:
            print("Invalid quantity!")

    def cancel_item(self):
        item = input("Enter item to cancel: ")
        if item in self.order:
            del self.order[item]
            print(RED + f"{item} removed from order" + RESET)

           
            self.orderjson = [self.order] 
            self.read_write.write_json(self.order_file, self.orderjson)
        else:
            print("Item not found in order!")

    def run(self):
        while True:
            print(SKY_BLUE + "\n<> FOOD ORDER MENU <>" + RESET)
            print("1. Order Food")
            print("2. Cancel Item")
            print("3. View Current Order")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.order_food()
            elif choice == "2":
                self.cancel_item()
            elif choice == "3":
                if self.order:
                    print("Current Order:")
                    for item, details in self.order.items():
                        print(f"{item}: {details['qty']} x {details['price']} = {details['qty']*details['price']}")
                else:
                    print("No items in order.")
            elif choice == "4":
                print("Exiting Food Order...")
                break
            else:
                print("Invalid choice, try again!")