from app.domain.read_write_json import json_methods
from app.dashboard.menu import ChoiceAdmin , ChoiceStaff
import getpass

class Login:
    def __init__(self):
        json_operations=json_methods()
        self.user_data=json_operations.read_json(r"app\database\manage.json")
    def identify_user(self):
        email = input("Enter your email id: ")
        password = getpass.getpass("Enter your passowrd: ")
        user_found= False
        
        for user in self.user_data:
            if user['email_id']==email and user['password']==password:
                user_found=True
                if user['role']=="staff":
                    print("WELCOME BACK STAFF MEMBER",user["username"])
                    ob1=ChoiceStaff()
                    ob1.show_menu_staff()
                  
                elif user['role']=="admin":
                    print("WELCOME BACK ",user["username"],"mam/sir.")
                    ob2=ChoiceAdmin()
                    ob2.show_menu_admin()
                   
        if not user_found:
            print("User not found")
            
                    