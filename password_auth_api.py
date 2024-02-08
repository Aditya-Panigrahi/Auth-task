from fetch_config import lock_limit, class_obj
credentials, locked_accounts = class_obj.dload_creds()

class Authenticator:
    @staticmethod
    def password_auth(username,password):
        user_data = credentials.get(username)
        successful_attempts = user_data.get("successful_attempts", 0)
        unsuccessful_attempts = user_data.get("unsuccessful_attempts", 0)
        lock_attempts = user_data.get("lock_attempts", 0)
        
        if password == credentials[username]["password"]:  
            successful_attempts += 1
            lock_attempts = 0
            user_data["successful_attempts"] = successful_attempts
            user_data["unsuccessful_attempts"] = 0
            response = f"Credentials match. Login successful!\nTotal attempts: {successful_attempts + unsuccessful_attempts}\nSuccessful attempts: {successful_attempts}\nUnsuccessful attempts: {unsuccessful_attempts}\n" 
            status = "success"  
            return response,status     
        else:
            unsuccessful_attempts += 1
            lock_attempts += 1
            user_data["unsuccessful_attempts"] = unsuccessful_attempts
            user_data["lock_attempts"] = lock_attempts
            response = f"Invalid credentials.\nTotal attempts: {successful_attempts + unsuccessful_attempts}\nSuccessful attempts: {successful_attempts}\nUnsuccessful attempts: {unsuccessful_attempts}\n"
            status = "fail"
            if lock_attempts >= lock_limit:
                response+="Your account has been locked."
                locked_accounts.append(username)
                class_obj.uload_creds(locked_accounts)
                
        return response,status
            