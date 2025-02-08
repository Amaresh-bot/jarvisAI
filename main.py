import speech_recognition as sr
import win32com.client
from pygame.transform import threshold
from wikipedia import languages

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def speak(text):
    speaker.Speak(text)

def takeCommand():
    """Function to take voice input from the user and return it as text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Adjust the pause threshold for better recognition
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-US")  # Use Google Speech Recognition
        print(f"User said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("Sorry, my speech service is down.")
        return None

if __name__ == "__main__":
    while True:
        print("Enter '1' to type text or '2' to speak (or 'exit' to quit):")
        choice = input().strip().lower()

        if choice == "1":
            print("Enter the text you want the computer to speak:")
            text = input().strip()
            if text.lower() == "exit":
                break
            speak(text)
        elif choice == "2":
            print("Speak now...")
            command = takeCommand()
            if command:
                speak(f"You said: {command}")
        elif choice == "exit":
            break
        else:
            print("Invalid choice. Please try again.")

