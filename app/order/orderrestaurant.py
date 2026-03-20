from app.dashboard.restaurant_menu import RestaurantMenu

class FoodOrder:
    def __init__(self, menu):
        self.menu = menu
        self.order = {}

    # Menu display
    def show_menu(self):
        for category, meals in self.menu.items():
            print(f"\n=== {category} ===")
            for meal_time, items in meals.items():
                print(f"\n-- {meal_time} --")
                for item, price in items.items():
                    print(f"{item} : ₹{price}")

    # Order food
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

            print(f"✅ {item} added to order")

        except:
            print("❌ Invalid input! Try again.")

    # Cancel order
    def cancel_item(self):
        item = input("Enter item to cancel: ")
        if item in self.order:
            del self.order[item]
            print(f"❌ {item} removed")
        else:
            print("Item not found!")

    # Billing
    def generate_bill(self):
        total = 0
        print("\n🧾 Your Bill")
        print("----------------------")
        for item, details in self.order.items():
            cost = details['price'] * details['qty']
            total += cost
            print(f"{item} x {details['qty']} = ₹{cost}")
        print("----------------------")
        print(f"Total = ₹{total}")
        print("🙏 Thank you!")


ob=FoodOrder()
ob.menu()
ob.order()