from app.domain.read_write_json import json_methods

class StaffManager:
    def __init__(self):
        self.jm = json_methods()
        self.input_path = r"D:\BabitaDanu_RMS_INDIXPERT\app\database\manage.json"
    def load_data(self):
        return self.jm.read_json(self.input_path)

    def remove_users(self):
        data = self.load_data()

        names_to_remove = input("Enter Staff usernames to remove : ")

        filtered_data = []

        for user in data:
            if user["username"] not in names_to_remove:
                filtered_data.append(user)

        self.jm.write_json(self.input_path, filtered_data)

        print("Please try again! only staff users removed!")

