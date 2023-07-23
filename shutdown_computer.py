from modules import *


class shutdown:
    def takecommands(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.speak("Listening")
            print("Listening...")
            r.pause_threshold = 0.7
            audio = r.listen(source, phrase_time_limit=5)
            try:
                self.speak("Recognizing")
                print("Recognizing...")
                query = r.recognize_google(audio, language="en-in")
                print("The query is printed = '", query, "'")
            except Exception as e:
                print(e)
                print("say that again please")
                return "None"
        return query

    def speak(self, audio):
        engine = pyttsx3.init("sapi5")
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[1].id)
        engine.say(audio)
        engine.runAndWait()

    def quitself(self):
        self.speak("do you want to shutdown the computer?")
        take = self.takecommands()
        choice = take
        if "yes" in choice:
            print("shutting down the computer...")
            self.speak("shutting down the computer")
            os.system("shutdown /s /t 10")
        elif "no" in choice:
            print("thank you")
            self.speak("thank you")


def close():
    maam = shutdown()
    maam.quitself()
