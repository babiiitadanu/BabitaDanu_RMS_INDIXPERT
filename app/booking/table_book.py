import json

SKY_BLUE = "\033[38;5;117m"
RED = "\033[31m"
RESET = "\033[0m"


class TableBookingSystem:
    def __init__(self):
        self.file_name = r"D:\BabitaDanu_RMS_INDIXPERT\app\database\tablebook.json"
        self.tables = self.load_data()

    def load_data(self):
        try:
            with open(self.file_name, "r") as f:
                return json.load(f)
        except:
            return {str(i): [] for i in range(1, 16)}

    def save_data(self):
        with open(self.file_name, "w") as f:
            json.dump(self.tables, f, indent=4)

    def show_menu(self):
        print("\n")
        print(SKY_BLUE + "<> TABLE MENU <>" + RESET)
        print(SKY_BLUE + "1." + RESET, "BOOK TABLE")
        print(SKY_BLUE + "2." + RESET, "VIEW BOOKINGS")
        print(SKY_BLUE + "3." + RESET, "CANCEL BOOKING")
        print(SKY_BLUE + "4." + RESET, "EXIT")
        print("\n")

    def show_tables(self):
        print(SKY_BLUE + "\n<> TABLE STATUS <>" + RESET)
        for table, bookings in self.tables.items():
            status = "Available" if not bookings else "Booked"
            print(f"Table {table} → {status}")
        print("\n")

    def book_table(self):
        try:
            self.show_tables()

            table_no = input("Enter table number (1-15): ")

            if table_no not in self.tables:
                print("Invalid table number!")
                return

            hours = int(input("Enter number of hours: "))
            seats = int(input("Enter number of seats (max 6): "))

            if seats > 6:
                print("Maximum 6 seats allowed per table!")
                return

            booking = {
                "hours": hours,
                "seats": seats
            }

            self.tables[table_no].append(booking)
            self.save_data()

            print(f"Table {table_no} booked for {hours} hours for {seats} people.")

        except ValueError:
            print("Please enter valid input.")

    def view_bookings(self):
        print(SKY_BLUE + "\n<> CURRENT BOOKINGS <>" + RESET)

        for table, bookings in self.tables.items():
            if bookings:
                print(f"\nTable {table}:")
                for b in bookings:
                    print(RED +f"Duration: {b['hours']} hours | Seats: {b['seats']}" + RESET)
            else:
                print(f"Table {table}: Available")

        print("\n")

    def cancel_booking(self):
        try:
            self.show_tables()

            table_no = input("Enter table number to cancel booking: ")

            if table_no not in self.tables:
                print("Invalid table number!")
                return

            if not self.tables[table_no]:
                print(f"Table {table_no} is already available.")
                return

           
            self.tables[table_no] = []
            self.save_data()

            print(RED + f"Booking for Table {table_no} has been cancelled." + RESET)

        except Exception as e:
            print("Error:", e)

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.book_table()
            elif choice == "2":
                self.view_bookings()
            elif choice == "3":
                self.cancel_booking()
            elif choice == "4":
                print("Exiting..")
                break
            else:
                print("Invalid choice, try again.")
                
                