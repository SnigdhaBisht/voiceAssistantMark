import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[1].id)

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour <18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
        
    speak("I am Mark. Please tell me how may I help you ?")
   
  


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... ")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        
    except Exception as e:
        print("Say that again please")
        return "None"
    
    return query




if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentence = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open('www.youtube.com')
            
        elif 'open google' in query:
            webbrowser.open('www.google.com')

        # elif 'play music' in query:
        #     music_dir=''
        #     songs =os.listdir(music_dir)
        # print(songs)
        # os.startfile(os.path.join(music_dir,songs[random.randit(0.len(songs))]))
        elif 'the time' in query:
            starTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is{strTime}")

        elif 'quit' in query:
            speak('Exiting. Thank you for talking to me today')
            sys.exit()

