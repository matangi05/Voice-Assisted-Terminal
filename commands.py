# import subprocess
# import os
# import platform

# def execute_command(intent_name, command_text=None):
#     if intent_name == "greeting":
#         print("Hello! How can I help you?")
#     elif intent_name == "goodbye":
#         print("Goodbye!")
#         exit()
#     elif intent_name == "no":
#         print("no")
#         exit()

#     elif intent_name == "open_file":
#         file_path="requirements.txt"
#         os.system(r'requirements.txt')
        
#     elif intent_name == "create_react_app" and command_text:
#         app_name = command_text.strip()
#         if app_name:
#             try:
#                 os.system(f'npm create vite@latest {app_name}')
#                 print(f"React app '{app_name}' created successfully.")
#             except Exception as e:
#                 print(f"An error occurred while creating React app: {e}")
#         else:
#             print("No app name provided.")
#     else:
#         print("Command not recognized.")


import os

def execute_command(intent_name, command_text=None, parameters={}):
    # Format the terminal command with the given parameters
    formatted_command = command_text.format(**parameters)
    os.system(formatted_command)
