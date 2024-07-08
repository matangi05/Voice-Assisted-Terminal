# import speech
# import intent
# import commands

# def main():
#     while True:
#         print("Listening...")
#         text = speech.listen_and_recognize()
#         if text:
#             intent_name,command_text = intent.determine_intent(text)
#             if intent_name:
#                 commands.execute_command(intent_name, command_text)
#             else:
#                 print("Sorry, I didn't understand that command.")

# if __name__ == "__main__":
#     main()

import speech
import intent
import commands

def main():
    while True:
        print("Listening for commands...")
        text = speech.listen_and_recognize()
        if text:
            intent_name, command_text, input_prompt = intent.determine_intent(text)
            parameters = {}

            # Prompt for parameters if any are needed
            if input_prompt:
                input_keys = [key.strip("{}") for key in command_text.split() if "{" in key and "}" in key]
                for key in input_keys:
                    prompt = input_prompt
                    if len(input_keys) > 1:
                        prompt = f"Please provide the {key.replace('_', ' ')}: "
                    parameters[key] = input(prompt)

            if intent_name:
                commands.execute_command(intent_name, command_text, parameters)
            else:
                print("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    main()
