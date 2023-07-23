import speech_recognition as sr
from bolna import speak


def TC():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}\n")
    except Exception as e:
        speak("say that again")
        query = None
    return query
