import subprocess
import os
import webbrowser

def main():
    venv_activate_script = r"D:\Python Training\.venv\Scripts\activate"  # Path to virtual environment activation script
    project_dir = r"D:\Python Training\.venv\Athreya-task\FastAPI"  # Path to your project directory

    # Activate virtual environment
    activate_command = f'cmd.exe /K "call {venv_activate_script}"'
    subprocess.Popen(activate_command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Change directory to your project directory
    os.chdir(project_dir)

    uvicorn_path = r"D:\Python Training\.venv\Scripts\uvicorn.exe"
    subprocess.Popen([uvicorn_path, "fast_api:app", "--reload"])
    
    # Open browser
    webbrowser.open("http://127.0.0.1:8000/docs")

if __name__ == "__main__":
    main()
