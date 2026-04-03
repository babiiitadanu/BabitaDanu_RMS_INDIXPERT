import json

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

path= r"app\database\menu.json"
class RestaurantMenu:

    def __init__(self):

        try:
            with open(path, "r") as file:
                self.menu = json.load(file)

        except FileNotFoundError:
            print("menu.json file not found!" )
            self.menu = {}

    def show_menu(self):

        for category in self.menu:
            print(YELLOW + f"\n    {category} MENU" + RESET)
            print(YELLOW + f"~~~~~~~~~~~~~~~~~~~~~" + RESET)
            

            for meal in self.menu[category]:
              
                print(GREEN + f"\n{meal}" + RESET)
               
                
                for item, price in self.menu[category][meal].items():
                 
                   print(f"{YELLOW}*{RESET} {item} : ₹{price}")
                    
                
    def update_menu(self):

        category = input("Enter Category (VEG/NON-VEG): ").upper()
        meal = input("Enter Meal (BREAKFAST/LUNCH/DINNER/DESSERTS/BEVERAGES): ").upper()
        item = input("Enter Item Name: ")
        price = (input("Enter New Price: "))

        if category in self.menu and meal in self.menu[category]:

            self.menu[category][meal][item] = price
            print(RED+"Menu Updated Successfully"+RESET )

            with open(path, "w") as file:
                json.dump(self.menu, file, indent=4)

        else:
            print(RED+"Invalid Category or Meal"+RESET)
            
    def delete_item(self):
        category = input("Enter Category (VEG/NON-VEG): ").upper()
        meal = input("Enter Meal (BREAKFAST/LUNCH/DINNER/DESSERTS/BEVERAGES): ").upper()
        item = input("Enter Item Name to delete: ")

        if category in self.menu:
            if meal in self.menu[category]:
                 if item in self.menu[category][meal]:

                    self.menu[category][meal].pop(item)
                    print("Item removed successfully")

                    with open(path, "w") as file:
                        json.dump(self.menu, file, indent=4)

                 else:
                     print("Item not found!")
                     
            else:
                print("Meal not found!")
                
        else:
            print("Category not found!")