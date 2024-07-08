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
