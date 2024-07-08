import os

def execute_command(intent_name, command_text=None, parameters={}):
    # Format the terminal command with the given parameters
    formatted_command = command_text.format(**parameters)
    os.system(formatted_command)
