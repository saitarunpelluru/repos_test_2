import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5')

voices=engine.getProperty('voices')
#print(voices[0].id)

engine.setProperty('voice',voices[0].id)

def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('pvstarun@gmail.com','email.password**')
    server.sendmail('pvstarun@gmail.com',to,content)
    server.close()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(" good morning bhuvan")

    elif hour>=12 and hour<18:
        speak("good afternoon bhuvan")
    else:
        speak("good evening bhuvan")

    speak("hey i am friday , your personnel voice assistant. please tell me how may i help you")           
def takecommand():
    #it takes comands
    r=sr.Recognizer() #class
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold =1 # pause threshold ante one of the parameter of speech recognition
         # pause_threshold ni ctrl and click chestha ardhamavuthadhi 
        audio = r.listen(source)
    try:
        print("recognizing....") 
        query=r.recognize_google(audio, language='en-in') 
        print(f"user said:{query}\n") 
    except Exception as e:
        #print(e)

        print("say that again please...") 
        return "None"   
    return query     


if __name__=="__main__":
    wishme()
    while True:
        query=takecommand().lower()
        #logic
        if 'wikipedia' in query:
            speak('searching wikipedia..')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        
        elif 'open youtube' in query: 
             webbrowser.open("youtube.com") 
        elif 'open google' in query: 
             webbrowser.open("google.com")
        elif 'open whatsapp' in query: 
             webbrowser.open("https://web.whatsapp.com/")
        elif 'play music' in query: 
            music_dir='C:\\Users\\Dell\\Documents\\music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is{strTime}")
        elif 'the date' in query:
            strDate=datetime.datetime.now()
            speak(f"the date is{strDate}")   
        elif 'open code ' in query:
            codepath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'send email to me' in query:
            try:
                speak("what should i say")
                content=takecommand()
                to="pvstarun@gmail.com"
                sendemail(to,content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry bhuvan unable to send the email")        