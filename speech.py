
import speech_recognition as sr

def listen_and_recognize():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"Recognized: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Error: {e}")
        return None

# curl.exe https://api.openai.com/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer sk-proj-U0Ohh9FFTN8rSv6yH2AxT3BlbkFJC1ytAWmnLEo0XC9H9egZ" -d '{ "model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": "Say this is a test!"}], "temperature": 0.7 }'