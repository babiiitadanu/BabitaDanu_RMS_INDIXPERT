from app.domain.read_write_json import json_methods
import uuid

RED = "\033[91m"
RESET = "\033[0m"

class UserSignup:

    def __init__(self):
        self.file_path = r"app\database\manage.json"
        self.json=json_methods()
        self.listdata = self.json.read_json(self.file_path)



    # Validation functions
    def validate_username(self, username):
        return username.isalpha()

    def validate_password(self, password):
        return len(password) >= 6

    def validate_role(self, role):
        role = role.lower()
        return role in ["admin", "staff"]

    def validate_email(self, email):
        if "@" not in email or "." not in email:
            return False
        at_index = email.index("@")
        dot_index = email.find(".")
        if at_index < 1 or dot_index < at_index or dot_index == len(email) - 1:
            return False
        return True

    def validate_aadhar(self, aadhar):
        return aadhar.isdigit() and len(aadhar) == 12

    def validate_phone(self, phone):
        return phone.isdigit() and len(phone) == 10

    def validate_address(self, address):
        return len(address.strip()) > 0

   
    def signup(self):
        data = {}
        data["id"] = uuid.uuid4().hex[:5]

        while True:
            new_username = input("ENTER USERNAME: ")
            if self.validate_username(new_username):
                data["username"] = new_username
                break
            else:
                print(RED+"INVALID USERNAME (only letters allowed!)"+RESET)

        while True:
            new_password = input("ENTER PASSWORD : ")
            if self.validate_password(new_password):
                data["password"] = new_password
                break
            else:
                print(RED+"INVALID PASSWORD (minimum 6 characters!)"+RESET)

        while True:
            role = input("ENTER ROLE (admin/staff): ")
            if self.validate_role(role):
                data["role"] = role
                break
            else:
                print(RED+"INVALID ROLE"+RESET)

        while True:
            email = input("ENTER EMAIL: ")
            if self.validate_email(email):
                data["email_id"] = email
                break
            else:
                print(RED+"INVALID EMAIL"+RESET)

        while True:
            aadhar = input("ENTER AADHAR NUMBER (12 digits): ")
            if self.validate_aadhar(aadhar):
                data["aadhar"] = aadhar
                break
            else:
                print(RED+"INVALID AADHAR NUMBER (must be 12 digits)"+RESET)

        while True:
            phone = input("ENTER PHONE NUMBER (10 digits): ")
            if self.validate_phone(phone):
                data["phone"] = phone
                break
            else:
                print(RED+"INVALID PHONE NUMBER (must be 10 digits)"+RESET)

        while True:
            address = input("ENTER ADDRESS: ")
            if self.validate_address(address):
                data["address"] = address
                break
            else:
                print(RED+"ADDRESS CANNOT BE EMPTY"+RESET)

        self.listdata.append(data)

    def write_file(self):
        try:
            self.json.write_json(self.file_path, self.listdata)
            print(RED+"SIGNUP SUCCESSFUL"+RESET)
        except Exception as e:
            print(e)

    def dashboard(self):
        self.signup()
        self.write_file()