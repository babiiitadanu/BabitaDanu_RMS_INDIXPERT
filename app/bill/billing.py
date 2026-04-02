from app.domain.read_write_json import json_methods

SKY_BLUE = "\033[38;5;117m"
RED = "\033[91m"
RESET = "\033[0m"

class RestaurantBill:
    def __init__(self): 
        self.order_file = r"app\database\order.json"

        reader = json_methods() 
        self.order_data = reader.read_json(self.order_file)

    def generate_bill(self):
        if not self.order_data:
            print(RED + "No items in the order!" + RESET)
            return

        customer_name = input("ENTER CUSTOMER NAME: ").strip()
        total = 0
        print(SKY_BLUE + f"\n<> BILL FOR {customer_name.upper()} <>\n" + RESET)

        for order in self.order_data:
            if customer_name in order:
                for item, details in order[customer_name].items():
                    cost = details['price'] * details['qty']
                    total += cost
                    print(f"{item:<15}: {details['qty']} x ₹{details['price']} = ₹{cost}")

        print(f"\nTotal = ₹{total}")
        print(RED + "Thank you!" + RESET)