I have created a project using which we can launch an application by creating the .exe file. When we start the application, it was ask for username and password, basically a login page. 
If the source in config.yml is json then it will read credentials from the modified_creds.json file, if source is mongo, then it will read from Mongo DB.
The username and password entered in the UI will be matched with the creds stores in mongo/json and give results accordingly.

Commands:
Create .exe file -> pyinstaller --onefile run_app.py
Run http server -> python -m http.server
Start Fast API -> uvicorn fast_api:app --reload
