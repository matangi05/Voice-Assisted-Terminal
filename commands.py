import subprocess

def execute_command(intent_name):
    if intent_name == "greeting":
        print("Hello! How can I help you?")
    elif intent_name == "goodbye":
        print("Goodbye!")
        exit()
    elif intent_name == "open_file":
        subprocess.run(["open", "requirements.txt"])  # Replace with your command to open a file
    else:
        print("Command not recognized.")
