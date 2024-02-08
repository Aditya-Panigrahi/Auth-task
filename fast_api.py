from fastapi import FastAPI, HTTPException,Body
from password_auth_api import Authenticator
from fetch_config import class_obj
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/login")
async def login(user_detail=Body()):
    credentials, locked_accounts = class_obj.dload_creds()
    try:
        stored_username = next(user for user, data in credentials.items() if data["username"] == user_detail['username'])
    except:
        return{"message":"User not found","status":"error"}
    if stored_username:
        if user_detail['username'] in locked_accounts:
            #raise HTTPException(status_code=404, detail="Account is locked") 
            return {"message": "Account is locked","status":"error"}
        response,status = Authenticator.password_auth(stored_username, user_detail['password'])
        return {"message": response,"status": status}
    

#uvicorn fast_api:app --reload