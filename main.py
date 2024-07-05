import speech
import intent
import commands

def main():
    while True:
        print("Listening...")
        command = speech.listen_and_recognize()
        if command:
            intent_name = intent.determine_intent(command)
            if intent_name:
                commands.execute_command(intent_name)
            else:
                print("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    main()
