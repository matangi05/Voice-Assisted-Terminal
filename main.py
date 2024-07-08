import speech
import intent
import commands
import gemini
def main():
    while True:
        print("Listening...")
        req = speech.listen_and_recognize()
        if req:
            command = gemini.get_command(req)
            commands.execute_command(command)

if __name__ == "__main__":
    main()
