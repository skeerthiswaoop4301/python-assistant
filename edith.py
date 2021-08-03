import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import pywhatkit as pw
import os
import webbrowser
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
# voices[0]=male voice
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendMail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('nagadeep.chandragiri@gmail.com','mylifedad143')
    server.sendmail('nagadeep.chandragiri@gmail.com',to,content)
    server.close()

def time():
    time=''
    time+="The Time is"
    time+=datetime.datetime.now().strftime("%Ihour %Mmin %Sseconds")
    speak(time)
def date():
    st="Todays Date is "
    day=int(datetime.datetime.now().day)
    month=int(datetime.datetime.now().month)
    year=int(datetime.datetime.now().year)
    speak(st)
    speak(day)
    speak(month)
    speak(year)
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)
        try:
            print("Recognizing...")
            query=r.recognize_google(audio,language='en-in')
        except Exception as e:
            print(e)
            speak("say that again please sir")
            return "None"
        return query

def authenticate():
    c=3
    speak("Please Say the Password")
    speak("You have 3 chances only")
    while(c!=0):
        passs=takecommand().lower()
        passs=passs.replace(' ','')
        print(passs)
        if passs=='pandu':
            return True
        else:
            c-=1
            speak("Wrong Password")
            speak("there are "+str(c)+"trails left")
    if(c==0):
        speak("Sorry and good bye")
        exit()
def greetings():
    authenticate()
    speak("Welcome Back Sir!")
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good Morning Sir!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon Sir!")
    elif hour>=18 and hour<24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")
    speak("This is Edith, How Can i help you?")


if __name__=='__main__':
    greetings()
    while True:
        query=takecommand().lower()
        if 'time now' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("searching")
            result=wikipedia.summary(query,sentences=2)
            speak(result)
        elif 'send mail' in query:
            try:
                speak("what should i say")
                content=takecommand()
                speak("to whome i should send")
                to=takecommand().lower()
                if 'at the rate' in to:
                    to.replace('attherate','@')
                if 'dot' in to:
                    to.replace('dot','.')
                ss=to.replace(' ','')
                print(ss)
                sendMail(ss,content)
                speak("Email was Sent")
            except Exception as e:
                speak("unable to send email")

        elif 'offline' in query:
            speak("Thank you sir! see you soon!")
            quit()
        elif 'search' in query:
            query=query.replace('search','')
            pw.search(query)
        elif 'youtube' in query:
            query=query.replace('on youtube','')
            query=query.replace('play','')
            pw.playonyt(query)
        elif 'log off' in query:
            speak("yes Sir!")
            speak("Thank you sir! see you soon!")
            
            os.system('shutdown -l')
            quit()
        elif 'shutdown' in query:
            speak("You Said to shutdown 4 3 2 1 ")
            os.system('shutdown /s /t 6')
        elif 'restart' in query:
            speak("You Said to restart 4 3 2 1 ")
            os.system('restart /r /t 6')
        elif 'note it down' in query:
            speak("Sure sir!")
            matter=takecommand().lower()
            rem=open('data.txt','w')
            speak("You Said to note "+ matter)
            rem.write(matter)
            speak("Done Sir!")
            rem.close()
        elif 'open google' in query:
            webbrowser.get(chrome_path).open('google.com')
        elif 'open youtube' in query:
            webbrowser.get(chrome_path).open('youtube.com')
        elif 'open c' in query:
            os.startfile('C:')
        elif 'open d' in query:
            os.startfile('D:')
        elif 'open e' in query:
            os.startfile('E:')
        elif 'open f' in query:
            os.startfile('F:')   
        elif 'open mycomputer' in query:
            os.startfile('This PC')

