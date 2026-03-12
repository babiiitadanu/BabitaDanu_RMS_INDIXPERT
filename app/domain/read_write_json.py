import json
class json_methods:
    def read_json(self,path):
        try:
            with open(path,'r') as file:
                data = json.loads(file.read())
                return data
        except Exception as e:
            return []
        
    def write_json(self,path,data):
        try:
            with open(path,'w') as file:
                file.write(json.dumps(data,indent=2))
        except Exception as e:
            print(e)
        