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
        self.order = {} 
        self.customer_name = ""

    def get_customer_name(self):
        while True:
            name = input("Enter Customer Name: ").strip()
            if name:
                self.customer_name = name
                break
            else:
                print(RED + "Customer name cannot be empty!" + RESET)

    def order_food(self):
        try:
            category = input("Enter Category (VEG/NON-VEG): ").upper()
            meal_time = input("Enter Meal Time (BREAKFAST/LUNCH/DINNER/DESSERTS): ").upper()
            item = input("Enter Item Name: ")

           
            price = int(self.menu[category][meal_time][item])

            qty = int(input("Enter Quantity: "))
            if qty > 500:
                print(RED + "You cannot order more than 500 of a single item!" + RESET)
                return

            
            if item in self.order:
                if self.order[item]['qty'] + qty > 500:
                    print(RED + "Total quantity for this item cannot exceed 500!" + RESET)
                    return
                self.order[item]['qty'] += qty
            else:
                self.order[item] = {'price': price, 'qty': qty}

            print(RED + f"{item} added to {self.customer_name}'s order" + RESET)

           
            existing_orders = self.read_write.read_json(self.order_file)
            if not isinstance(existing_orders, list):
                existing_orders = []

            existing_orders.append({self.customer_name: {item: {'price': price, 'qty': qty}}})
            self.read_write.write_json(self.order_file, existing_orders)

        except KeyError:
            print(RED + "Item not found in menu! Check category, meal time, and item name." + RESET)
        except ValueError:
            print(RED + "Invalid quantity! Enter a number." + RESET)
        except Exception as e:
            print(RED + f"Unexpected error: {e}" + RESET)

    def cancel_item(self):
        try:
            item = input("Enter item to cancel: ")

            if item in self.order:
                qty_removed = self.order[item]['qty']
                del self.order[item]
                print(RED + f"{item} removed from {self.customer_name}'s order" + RESET)

                existing_orders = self.read_write.read_json(self.order_file)
                if not isinstance(existing_orders, list):
                    existing_orders = []

                
                existing_orders.append({self.customer_name: {item: {'price': 0, 'qty': -qty_removed}}})
                self.read_write.write_json(self.order_file, existing_orders)

            else:
                print(RED + "Item not found in order!" + RESET)
        except Exception as e:
            print(RED + f"Unexpected error: {e}" + RESET)

    def run(self):
        self.get_customer_name()  
        while True:
            print(SKY_BLUE + f"\n<> FOOD ORDER MENU for {self.customer_name} <>" + RESET)
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
                    print(f"Current Order for {self.customer_name}:")
                    for item, details in self.order.items():
                        print(f"{item}: {details['qty']} x {details['price']} = {details['qty']*details['price']}")
                    total = sum(details['qty']*details['price'] for details in self.order.values())
                    print(f"Total = ₹{total}")
                else:
                    print("No items in order.")
            elif choice == "4":
                print(f"Exiting {self.customer_name}'s Food Order...")
                break
            else:
                print(RED + "Invalid choice, try again!" + RESET)