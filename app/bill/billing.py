from app.dashboard.restaurant_menu import RestaurantMenu
from app.order.orderrestaurant import FoodOrder

SKY_BLUE = "\033[38;5;117m"
RED = "\033[91m"
RESET = "\033[0m"

        
class RestaurantBill:
    def __init__(self, order):
        self.order = order

    def generate_bill(self):
        if not self.order:
            print(RED+ "No items in the order!" + RESET)
            return

        total = 0
        print(SKY_BLUE + "\n<> YOUR BILL <>\n" + RESET)
        for item, details in self.order.items():
            cost = details['price'] * details['qty']
            total += cost
            print(f"{item} x {details['qty']} = ₹{cost}")
        print(f"\nTotal = ₹{total}")
        print(RED+"Thank you!"+RESET)
        
    