## code by abhay jaiswal
import pyttsx3 #python text to speech
import speech_recognition as sr #speech recognition
import wikipedia #wikipedia
import webbrowser #working with web browser and its contro
import os  #to access the cmd of windows operating system
import datetime # access the current date and time of the machine
import pyjokes #for python jokes update
import smtplib #for emails
import pyaudio
import random
from googlesearch import search
from PyDictionary import PyDictionary
dictionary=PyDictionary()
import pywhatkit


engine=pyttsx3.init('sapi5') #engine is object of pyttsx class 
voices=engine.getProperty('voices') #voices can hold the property 
engine.setProperty('voice', voices[1].id) #set the voice 0 for male 1 for female
engine.setProperty('rate', 100)
def speak(audio):     #function to let app. speak
    engine.say(audio) #audio as parameter to say whaat is audio
    engine.runAndWait() #run and wait for a while

def wishme():         #wish me according to time
    hour=int(datetime.datetime.now().hour)  #take time from system change in hour
    if hour>=0 and hour<12:
        speak("hey A B, Good morning!")
    elif hour>=12 and hour<18:
        speak("hey A B, Good afternoon!")
    else:
        speak("hey A B, Good evening!")
    speak("i am mark, your voice assistant, what can i do for you?")


def takecmd():  #takes input from microphone convert it into command
    r=sr.Recognizer()  # create object of Recognizer
    with sr.Microphone() as source: #use microphone as source input
        print("Listening...")
        #r.pause_threshold=1  #waiting time to let user finish their query
        audio=r.listen(source) #listen function to listen input
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en_in') #recognize voice and change into text from google
        query=query.lower() #lower the query
        print(query)## code by abhay jaiswal
        
    except Exception as e:
        print("say that again please...")
        return "None"
    return query
    

def run_mark():             #base function that can contain the ways to work
    command=takecmd()
    if 'play song' in command:
        play_song()
        print('here\'s my choice for you...enjoy!')
    elif 'open firefox' in command:
        firefox()
    elif 'open code' in command:
        visual_code()
    elif 'open file explorer' in command:
        files()
    elif 'open google'in command:
        ggl()
    elif 'open youtube' in command:
        yt()
    elif 'open facebook' in command:
        fb()
    elif 'who is' in command:
        command.replace('who is', '')## code by abhay jaiswal
        wikii(command)
    elif 'what is' in command:
        cmm=command.replace('what is', '')
        ggr(cmm)
    elif 'meaning of' in command:
        dicto(command)
    elif 'open notepad' in command:
        npad()
    elif 'open paint' in command:
        paint()
    elif 'open calculator'in command:
        calc()
    elif 'open photoshop' in command:
        photoshop()
    elif 'open screen recorder' in command:
        record()
    elif 'open command prompt' in command:
        cmd()
    elif 'clock time' in command:
        time()
    elif 'crack a joke' in command:
        joke()
    elif 'on youtube' in command:
        ytplay(command)
    elif 'play video' in command:
        os.startfile('D:\\videos\\thor.mp4')## code by abhay jaiswal
    elif 'how are you ' in command:
        care()
    elif 'who created you' in command:
        print('ABHAY JAISWAL')
        speak('master abhay jayswal created me')
    elif 'the best person of the world' in command:
        print('ABHAY JAISWAL')
        speak('according to me the best person of the world is abhay jayswal, who created me')
    elif 'close yourself'in command:
        speak("thank you very much to use me sir, see you soon, take care")
        exit()
    elif 'how to shutdown pc' in command:
        print('Alt+F4')
        speak('press alt and F 4 simultaniously')
    elif 'add' in command: #add no and no
        add(command)
    elif 'multiply' in command: #multpy no to no
        multi(command)
    elif 'subtract' in command: #subtract no from no
        sub(command)
    elif 'divide' in command: #div no by no
        div(command)
    elif 'tell me about yourself' in command:
        speak('i am jenny your voice assistant, created by abhay jayaswal, on visual code, in python language, i am plateform independent, i can do many things for you just you have to command me, we can be best friend if you understand me, you can teach me much more if you know python programming language')
    elif 'what do you think' in command:
        speak('Love and affection are two inseparable feelings. Love is often described or defined as a deep affection whereas affection is a feeling of liking and fondness. However, we’ll look at these feelings separately in order to examine the difference between love affection. The main difference between love and affection is that love is deeper and stronger than affection. If we love someone, we’ll feel affection for that person, but we don’t love everyone we feel affection for')
    
def add(command):
    list=[]
    list=command.split()
    result=(int(list[1])+int(list[3]))
    print(result)
    speak(result)

def multi(command):
    list=[]
    list=command.split()
    result=(int(list[1])*int(list[3]))
    print(result)

    speak(result)

def sub(command):
    list=[]
    list=command.split()## code by abhay jaiswal
    result=(int(list[1])-int(list[3]))
    print(result)
    speak(result)

def div(command):
    list=[]
    list=command.split()
    result=(int(list[1])/int(list[3]))
    print(result)
    speak(result)

def care():
    speak("i am fine sir, thank you")

def ytplay(command):
    song=command.replace('on youtube', '')
    song=song.replace('play', '')
    print(song)
    speak('playing, ' + song)
    pywhatkit.playonyt(song)

def joke():
    speak(pyjokes.get_joke())

def time():
    time = datetime.datetime.now().strftime('%I:%M %p')
    speak('Current time is ' + time)

def cmd():
    os.startfile('C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk')

def record():
    os.startfile('C:\Program Files (x86)\Aiseesoft Studio\Aiseesoft Screen Recorder\Aiseesoft Screen Recorder.exe')
    
def photoshop():
    os.startfile('C:\Program Files (x86)\Adobe Photoshop CS6\Photoshop.exe')

def calc():## code by abhay jaiswal
    os.startfile('C:\Windows\System32\calc.exe')

def paint():
    os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Paint.lnk')

def npad():
    os.startfile('C:\\Windows\\notepad.exe')

def dicto(cmm):
    cmm=cmm.replace('meaning of ', '')
    result=dictionary.meaning(cmm)
    final='the meaning of '
    final=final+cmm+' is '
    speak(final)
    print(result)
    speak(result)

def ggr(cmm):
     speak('searching web...') 
     webbrowser.open('https://google.com/search?q=%s' % cmm)
     speak("here are your result")
     
def wikii(cmm):
    speak('searching wikipedia...')
    result=wikipedia.summary(cmm,sentences=3)
    speak('According to wikipedia')
    print(result)
    speak(result)

def fb():
    webbrowser.open('facebook.com')

def yt():
    webbrowser.open('youtube.com')

def ggl():
    webbrowser.open('google.in')

def files():
    f_path='C:\Windows\explorer.exe'
    os.startfile(f_path)

def visual_code():
    vs_path='C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\code'
    os.startfile(vs_path)

def firefox():
    firefox_path='C:\\Program Files (x86)\\Mozilla Firefox\\firefox'
    os.startfile(firefox_path)
        
def play_song():
    music_path='D:\\songs'  #path is D:\songs
    songs=os.listdir(music_path) 
    si=random.randint(0,100)
    os.startfile(os.path.join(music_path,songs[si]))

if __name__ == "__main__":
    wishme()
    while True:
        run_mark()
