I have created a project using which we can launch an application by creating the .exe file. When we start the application, it will ask for username and password, basically a login page. 
If the source in config.yml is json then it will read credentials from the modified_creds.json file, if source is mongo, then it will read from Mongo DB.
The username and password entered in the UI will be matched with the creds stores in mongo/json and give results accordingly.

Features:
- Total attempts, successful, and unsuccessful attempts which a user has made to login are shown as "stats".
- Successful login will take to success page where "stats" will be shown.
- Unsuccessful/Invalid login will bring a toaster showing appropriate message.
- 3 time entering incorrect password will make the user locked. And further entring correct password also won't make the login successful.

Commands:
Create .exe file -> pyinstaller --onefile run_app.py
Run http server -> python -m http.server
Start Fast API -> uvicorn fast_api:app --reload
Switch to .venv in VS Code by runing the script -> Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
                                                -> cd ./venv/Scripts
                                                -> activate