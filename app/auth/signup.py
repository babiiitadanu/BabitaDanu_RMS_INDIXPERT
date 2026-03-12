import json
import uuid


class UserSignup:

    def __init__(self):
        self.file_path = r"app\database\manage.json"
        self.listdata = []

    def read_file(self):
        try:
            with open(self.file_path, "r") as file:
                self.listdata = json.load(file)
        except:
            self.listdata = []

   
    def validate_username(self, username):
        if username.isalpha():
            return True
        return False

   
    def validate_password(self, password):
        if len(password) >= 6:
            return True
        return False

    
    def validate_role(self, role):
        role = role.lower()
        if role == "admin" or role == "staff":
            return True
        return False

    
    def validate_email(self, email):

        if "@" not in email:
            return False

        if "." not in email:
            return False

        at_index = email.index("@")
        dot_index = email.find(".")

        if at_index < 1:
            return False

        if dot_index < at_index:
            return False

        if dot_index == len(email) - 1:
            return False

        return True

    def signup(self):

        data = {}
        data["id"] = uuid.uuid4().hex[:5]

       
        while True:
            new_username = input("ENTER USERNAME: ")
            if self.validate_username(new_username):
                data["username"] = new_username
                break
            else:
                print("INVALID USERNAME (only letters allowed!)")


        while True:
            new_password = input("ENTER PASSWORD : ")
            if self.validate_password(new_password):
                data["password"] = new_password
                break
            else:
                print("INVALID PASSWORD (only 6 letters allowed!)")

        
        while True:
            role = input("ENTER ROLE (admin/staff): ")
            if self.validate_role(role):
                data["role"] = role
                break
            else:
                print("INVALID ROLE")

        
        while True:
            email = input("ENTER EMAIL: ")
            if self.validate_email(email):
                data["email_id"] = email
                break
            else:
                print("INVALID EMAIL")

        self.listdata.append(data)

    def write_file(self):
        try:
            with open(self.file_path, "w") as file:
                json.dump(self.listdata, file, indent=4)
                print("SIGNUP SUCCESSFUL")
        except Exception as e:
            print(e)

        
    def dashboard(self):
        self.read_file()
        self.signup()
        self.write_file()
