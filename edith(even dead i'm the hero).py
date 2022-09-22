from modules import *
from bolna import speak
from take_command import TC
from birthdaywisher import birthdays
from weather import report
print("Intilizing EDITH...")
speak("Initializing EDITH")
name="mehul"
#birthdays()
print(f"how may i help you? {name}")
speak("How may i help you?"+name+'.')
while True:
    query=TC()
    if query==None:
        pass
    elif 'Wikipedia' in query or 'wikipedia' in query:
        speak("searching wikipedia......")
        query=query.replace('wikipedia','')
        result=wikipedia.summary(query,sentences=5)
        print(result)
        speak(result)
    elif 'Calculator' in query or 'open Calculator' in query:
        from calculator import *
    elif 'tell me something about you' in query.lower().split():
        print("I am FRIDAY an AI assistent created by Mehul Verma. I am still not complete but my creator tried hard to create me!")
        speak('I am FRIDAY an AI assistent created by Mehul Verma ... I am still not complete ... but my creator tried hard to create me!')
    elif 'tell me a joke' in query.lower().split():
        print("Two boys were arguing when the teacher entered the room.") 
        print("The teacher says, 'Why are you arguing?'")
        print("One boy answers, 'We found a ten dollor bill and decided to give it to whoever tells the biggest lie.'")
        print('"You should be ashamed of yourselves," said the teacher, "When I was your age I did not even know what a lie was."')
        print("The boys gave the ten dollars to the teacher.")
        speak("Two boys were arguing when the teacher entered the room ... The teacher says, 'Why are you arguing?' ... One boy answers, 'We found a ten dollor bill and decided to give it to whoever tells the biggest lie.' ... 'You should be ashamed of yourselves,' said the teacher, 'When I was your age I did not even know what a lie was.' ... The boys gave the ten dollars to the teacher.")
    elif 'open Settings' in query or 'settings' in query:
        os.system('control.exe')
    elif 'open CMD' in query or 'CMD' in query or 'cmd' in query:
        os.system('cmd.exe')
    elif 'open Epic' in query or 'open epic' in query:
        w="D:\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
        os.startfile(w)
    elif 'open Word'in query or 'open microsoft word' in query or 'word' in query:
        word="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
        os.startfile(word)
    elif 'open PowerPoint'in query or 'open microsoft powerpoint' in query or 'powerpoint' in query:
        powerpoint="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
        os.startfile(powerpoint)
    elif 'open Excel'in query or 'open microsoft excel' in query or 'excel' in query:
        excel="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"
        os.startfile(excel)
    elif 'play Rock paper scissors'in query or 'play RPS' in query or 'RPS' in query:
        from rps import game
        game()
    elif 'shutdown' in query or 'shutdown the computer' == query or 'Shutdown' in query:
        from shutdown_computer import *
        close()
    elif 'Chess' in query or 'play Chess' in query:
        from chess import *
    elif 'days to my birthday' in query:
        from days_to_birthday import bday
        bday()
    elif 'minwsweeper' in query or 'play Minesweeper' in query:
        from minesweeper import *
    elif 'pong' in query or 'play Pong' in query:
        from pong import *
    elif 'weather report' in query:
        report()
    elif 'stopwatch' in query:
        from stopwatch import *
    elif 'timer' in query:
        from timer import *
    elif 'specs' in query or 'laptop specs' in query:
        my_system = platform.uname()
        print(f"System: {my_system.system}")
        print(f"Node Name: {my_system.node}")
        print(f"Release: {my_system.release}")
        print(f"Version: {my_system.version}")
        print(f"Machine: {my_system.machine}")
        print(f"Processor: {my_system.processor}")
        speak("checking CPU and RAM usage...")
        print('The CPU usage is: ', psutil.cpu_percent(4))
        print('RAM memory % used:', psutil.virtual_memory()[2])
    elif 'open YouTube' in query or 'youtube' in query or 'Youtube' in query or 'YouTube' in query or 'Youtube' in query:
        webbrowser.open('https://www.youtube.com/')
    elif 'whatsapp' in query or 'Whatsapp' in query or 'WhatsApp' in query or 'web Whatsapp' in query:
        webbrowser.open('https://web.whatsapp.com/')
    elif "exit" in query.lower().split() or "bye" in query.lower().split() or "sleep" in query.lower().split() or "close" in query.lower().split():
            speak("Ok bye, "+name+'.')
            print(f"Ok bye, {name}")
            break
    elif 'time' in query.lower().split():
        t = time.localtime()
        ct=time.strftime("%H:%M:%S")
        print(ct)
        speak(ct)
    elif "date" in query.lower().split():
        now = datetime.datetime.now()
        print (now.strftime("%d-%m-%y"))
        speak (now.strftime("%d-%m-%y"))
    elif 'fortnite' in query.lower().split():
        if 'fortnite' in query:
            f='C:\\Users\\mehul\\Desktop\\Fortnite.url'
            os.startfile(f)
        else:
            os.startfile('C:\\Users\\mehul\\Desktop\\Fortnite.url')
    elif "send mail" in query.lower().split():
        from send_mail import sendEmail
        sendEmail()
    elif "send email to dummy" in query.lower().split():
        try:
            speak("what should i say?")
            content=TC()
            to="lghtnngfast@gmail.com"
            sendEmail(to,content)
            speak("email has been sent")
        except Exception as e:
            print(e)
            speak("sorry master i was unable to send this mail.")
    else :
        try:
            from googlesearch import search 
        except ImportError: 
	        print("No module named 'google' found")
        l=[]
        for j in googlesearch.search(query):
            l.append(j)
        webbrowser.open(l[0])