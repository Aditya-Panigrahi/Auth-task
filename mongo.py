from fetch_config import client

class Mongo:
    def dload_creds():  
        try:
            db = client["credential_task"]  
            collection = db["credentials"]
            data = collection.find_one()  
            credentials = data["credentials"]
            locked_accounts = data["locked_list"]
            return credentials,locked_accounts
        except:
            print("Error in db connection or data fetching")
    
    def uload_creds(upload_data):
        db = client["credential_task"]  
        collection = db["credentials"]
        collection.update_one({}, {"$set": {"locked_list": upload_data}})