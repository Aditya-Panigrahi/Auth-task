import json
from fetch_config import json_file_path

class Json:
    def dload_creds():
        try:
            with open(json_file_path) as my_file:
                data = json.load(my_file)
                credentials = data["credentials"]
                locked_accounts = data["locked_list"]
            return credentials,locked_accounts
        except:
            print("file path not found")
    
    def uload_creds(upload_data):
        try:
            with open(json_file_path) as my_file:
                content = json.load(my_file)
                content['locked_list'] = upload_data
            with open(json_file_path,'w') as my_file:
                json.dump(content,my_file,indent=2)
        except:
            print("file path not found")