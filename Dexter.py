import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser 
import os 
import random 
import smtplib 


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<17:
        speak("Good Afternoon!")
    elif hour>=17 and hour<21:
        speak("Good Evening!")
    else:
        speak("Good Night!")

    speak("Hello! I am Dexter. How may I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Please! Say it again..")
        return "None"

    return query 


def there_exists(terms):
    for term in terms:
        if term in query:
            return True


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('krups4444@gmail.com', 'password')
    server.sendmail('krups4444@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while 1:
        query = takeCommand().lower()


        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("opening youtube, please wait")


        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google, please wait")


        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("opening stackoverflow, please wait")


        elif 'open amazon' in query or 'shop online' in query:
            webbrowser.open("https://www.amazon.com")
            speak("opening amazon, please wait")


        elif 'weather' in query or 'shop online' in query:
            webbrowser.open("https://www.accuweather.com/en/in/ahmedabad/202438/current-weather/202438")
            speak("showing you today's weather forecast, please wait")


        elif 'play music' in query:
            music_dir = 'D:\my music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))


        elif there_exists(["exit", "quit", "goodbye"]):
                speak("Goodbye Krupa..!")
                exit()


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Hey Krupa, the time is {strTime}")


        elif 'news' in query:
            webbrowser.open("https://www.indiatoday.in/")
            speak("opening today's news, please wait")


        elif 'open vs code' in query:
            codePath = "D:\Microsoft VS Code\Code.exe"
            os.startfile(codePath)
            speak("opening v s code, please wait")


        elif 'teams' in query:
            codePath = "C:\\Users\\krupa\\AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe"
            os.startfile(codePath)
            speak("opening teams, please wait")


        elif there_exists(["plus","minus","multiply","by","power","+","-","*","/"]):
            opr = query.split()[1]

            if opr == '+':
                print(int(query.split()[0]) + int(query.split()[2]))
                speak(int(query.split()[0]) + int(query.split()[2]))

            elif opr == '-':
                print(int(query.split()[0]) - int(query.split()[2]))
                speak(int(query.split()[0]) - int(query.split()[2]))

            elif opr == 'multiply' or 'x':             
                print(int(query.split()[0]) * int(query.split()[2]))
                speak(int(query.split()[0]) * int(query.split()[2]))

            elif opr == 'by':
                print(int(query.split()[0]) / int(query.split()[2]))
                speak(int(query.split()[0]) / int(query.split()[2]))

            elif opr == 'power':
                print(int(query.split()[0]) ** int(query.split()[2]))
                engine.say(int(query.split()[0]) ** int(query.split()[2]))
                
            else:
                engine.say("Wrong Operator")


        elif 'email to krupa' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = "krups4444@gmail.com"
                sendEmail(to, content)
                speak("Krupa, your email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Krupa, I am not able to send this email.")

        

     

    

