# # Example intent determination function
# def determine_intent(text):
#     text=text.lower()
#     # Implement your intent recognition logic here
#     if "hello" in text:
#         return "greeting", None
#     elif "goodbye" in text:
#         return "goodbye", None
#     elif "no" in text:
#         return "no", None
#     elif "open file" in text:
#         return "open_file", None
#     elif "create a react app" in text:
#         return "create_react_app", text.replace("create react app", "").strip()
#     else:
#         return None

import pickle
import pandas as pd

# Load the trained model
with open("intentmodel.pkl", "rb") as f:
    model = pickle.load(f)

# Load the dataset with terminal commands
data = pd.read_csv("dataset.csv")

def determine_intent(text):
    intent = model.predict([text])[0]
    command_row = data[data['intent'] == intent].iloc[0]
    terminal_command = command_row['terminal_command']
    input_prompt = command_row['input_prompt'] if pd.notna(command_row['input_prompt']) else ""
    return intent, terminal_command, input_prompt
