SKY_BLUE = "\033[38;5;117m"
RESET = "\033[0m"


class RestaurantBill:

    def __init__(self):
      
        self.burger_price = 120
        self.pizza_price = 250
        self.cold_drink_price = 40

       
    
        self.burger_qty = 1
        self.pizza_qty = 1
        self.cold_drink_qty = 1

    def calculate_bill(self):
        
        self.burger_total = self.burger_price * self.burger_qty
        self.pizza_total = self.pizza_price * self.pizza_qty
        self.cold_drink_total = self.cold_drink_price * self.cold_drink_qty

        
        self.subtotal = self.burger_total + self.pizza_total + self.cold_drink_total
        self.total = self.subtotal + self.gst

    def print_bill(self):
        print(SKY_BLUE + " RESTAURANT BILL " + RESET)
        print("Item\tQty\tPrice")

        print(f"Burger\t{self.burger_qty}\t₹{self.burger_total}")
        print(f"Pizza\t{self.pizza_qty}\t₹{self.pizza_total}")
        print(f"Cold drink\t{self.cold_drink_qty}\t₹{self.cold_drink_total}")

        print("")
        print(f"Subtotal:\t₹{self.subtotal}")
        print(f"GST (5%):\t₹{self.gst}")
        print(f"Total:\t₹{self.total}")


def main():
    bill = RestaurantBill()
    bill.calculate_bill()
    bill.print_bill()


if __name__ == "__main__":
    main()