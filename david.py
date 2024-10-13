import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon!") 

    elif hour>=1 and hour<5 or hour>=21 and hour<24:
        speak("Good Night!")

    else:
        speak("Good Evening!")  

    speak("I am David Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('Youremail@gmail.com', 'password')
        server.sendmail('youremail@gmail.com', to, content)
        server.close()
        
        speak("Email sent successfully!")
        print("Email sent successfully!")

    except Exception as e:

        print(f"Error:{e}")
        speak("sorry,I couldn't send the email")

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            if "search" in query:
                query = query.replace("search", "")
                results = wikipedia.search(query)
                speak(f"Here are some search results from Wikipedia: {results}")
                print(results)
            else:
                results = wikipedia.summary(query, sentences=2)
                speak(f"According to Wikipedia, {results}")
            
        elif "who are you" in query:
            speak("I am your virtual assistant created by Pratik")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            print("Here's the code:")
            print(open(__file__, 'r').read())

        elif 'send email' in query:
            to = input("Enter the recipient's email address: ")
            content = input("Enter the email content: ")
            sendEmail(to, content)

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r") 
            print(file.read())
            speak(file.read(6))

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
