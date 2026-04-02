from app.domain.read_write_json import json_methods
from datetime import datetime


SKY_BLUE = "\033[38;5;117m"
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"


TIME_SLOTS = [
    "10 AM - 12 PM",
    "12 PM - 2 PM",
    "2 PM - 4 PM",
    "4 PM - 6 PM",
    "6 PM - 8 PM",
    "8 PM - 10 PM"
]

class TableBookingSystem:
    def __init__(self):
        self.file_name = r"app\database\tablebook.json"
        self.log_file = r"app\database\booking_log.txt"
        self.tables = self.load_data()

    def log_action(self, action, table_no=None, slot=None, seats=None, name=None):
        """Log all actions to a file with timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {action}"
        if table_no:
            entry += f" | Table: {table_no}"
        if slot:
            entry += f" | Slot: {slot}"
        if seats:
            entry += f" | Seats: {seats}"
        if name:
            entry += f" | Name: {name}"
        with open(self.log_file, "a") as f:
            f.write(entry + "\n")

    def load_data(self):
        try:
            return json_methods.read_json(self.file_name)
        except:
            return {
                str(i): {slot: None for slot in TIME_SLOTS}
                for i in range(1, 36)
            }

    def save_data(self):
        try:
            json_methods.write_json(self.file_name, self.tables)
        except Exception as e:
            print(RED + f"Error saving data: {e}" + RESET)

    def show_menu(self):
        print("\n")
        print(SKY_BLUE + "<> TABLE MENU <>" + RESET)
        print(SKY_BLUE + "1." + RESET, "BOOK TABLE")
        print(SKY_BLUE + "2." + RESET, "VIEW BOOKINGS")
        print(SKY_BLUE + "3." + RESET, "CANCEL BOOKING")
        print(SKY_BLUE + "4." + RESET, "EXIT")
        print("\n")

    def show_tables(self):
        print(SKY_BLUE + "\n TABLE STATUS " + RESET)
        for table, slots in self.tables.items():
            print(RED + f"\n  Table {table}:" + RESET)
            for slot, booking in slots.items():
                status = f"{GREEN}Available{RESET}" if booking is None else f"{RED}Booked{RESET}"
                print(f"  {slot} → {status}")
        print("\n")

    def book_table(self):
        try:
            self.show_tables()
            table_no = input("Enter table number (1-35): ")

            if table_no not in self.tables:
                print(RED + "Invalid table number!" + RESET)
                return

            print(SKY_BLUE + "\nAvailable Time Slots:" + RESET)
            for slot in TIME_SLOTS:
                print(slot)

            slot = input("Enter time slot: ")

            if slot not in TIME_SLOTS:
                print(RED + "Invalid time slot!" + RESET)
                return

            if self.tables[table_no][slot] is not None:
                print(RED + "This slot is already booked!" + RESET)
                return

            name = input("Enter your name: ")

            seats = int(input("Enter number of seats (max 6): "))
            if seats > 6:
                print(RED + "Maximum 6 seats allowed!" + RESET)
                return

            booking = {"name": name, "seats": seats}
            self.tables[table_no][slot] = booking
            self.save_data()

            print(GREEN + f"Table {table_no} booked for {slot} for {seats} people under name {name}." + RESET)
            self.log_action("BOOKED", table_no, slot, seats, name)

        except ValueError:
            print(RED + "Invalid input." + RESET)

    def view_bookings(self):
        print(SKY_BLUE + "\n CURRENT BOOKINGS " + RESET)
        for table, slots in self.tables.items():
            print(RED + f"\nTable {table}:" + RESET)
            for slot, booking in slots.items():
                if booking:
                    print(RED + f"{slot} → Name: {booking['name']}, Seats: {booking['seats']}" + RESET)
                else:
                    print(GREEN + f"{slot} → Available" + RESET)
        print("\n")

    def cancel_booking(self):
        self.show_tables()
        table_no = input("Enter table number: ")

        if table_no not in self.tables:
            print(RED + "Invalid table!" + RESET)
            return

        slot = input("Enter slot to cancel: ")

        if slot not in TIME_SLOTS:
            print(RED + "Invalid slot!" + RESET)
            return

        if self.tables[table_no][slot] is None:
            print(GREEN + "Already available!" + RESET)
            return

        name = input("Enter your name for verification: ")
        if self.tables[table_no][slot]["name"].lower() != name.lower():
            print(RED + "Name does not match booking! Cannot cancel." + RESET)
            return

        seats = self.tables[table_no][slot]["seats"]
        self.tables[table_no][slot] = None
        self.save_data()

        print(RED + f"Booking cancelled for Table {table_no}, Slot {slot}" + RESET)
        self.log_action("CANCELLED", table_no, slot, seats, name)

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
                print(RED + "Exiting.. Hotel Closed after 10 PM" + RESET)
                break
            else:
                print(RED + "Invalid choice, try again." + RESET)


