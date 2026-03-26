import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import time


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) 

def konus(metin):
    engine.say(metin)
    engine.runAndWait()

def komut_dinle():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening, sir...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source) 
        audio = r.listen(source)

    try:
        print("Recognizing...")
        komut = r.recognize_google(audio, language='en-US')
        print(f"You said: {komut}\n")
    except Exception as e:
        print("I didn't quite catch that, sir. Could you repeat?")
        return "None"
    
    return komut.lower()

def sistemleri_baslat():
    konus("Welcome sir. Systems are coming online.")
    
    # 1.Open Media (YouTube/Spotify)
    print("Opening media...")
    #Enter your link below 
    media_url = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID" 
    webbrowser.open(media_url)

    time.sleep(1)

    # 2.Prepare Workspace via VS Code
    print("Preparing the workspace...")
    # Make sure you enter your project file path below
    proje_dosyasi = r"C:\PATH\TO\YOUR\PROJECT\file.py" 
    os.system(f'code "{proje_dosyasi}"')
    
    time.sleep(2)

    # 3.Starting APP 
    print("Starting AI assistant...")
    # Enter your app path (you can change the app I just use claude)
    ai_app_path = r"C:\PATH\TO\YOUR\APP\Claude.exe" 
    
    try:
        os.startfile(ai_app_path)
    except FileNotFoundError:
        hata_mesaji = "Executable not found in the specified path, sir."
        print(hata_mesaji)
        konus(hata_mesaji)
    except PermissionError:
        hata_mesaji = "Access denied to the folder, sir. Permission settings may need adjustment."
        print(hata_mesaji)
        konus(hata_mesaji)

# Main Loop
if __name__ == "__main__":
    konus("System is on standby. Awaiting your command, sir.")
    while True:
        gelen_komut = komut_dinle()
        
        if 'wake up' in gelen_komut or 'start systems' in gelen_komut:
            sistemleri_baslat()
            konus("All systems have been activated. Do you have another command, sir?")
            
        elif 'thank you' in gelen_komut or 'exit' in gelen_komut or 'shut down' in gelen_komut:
            konus("Systems are shutting down. Have a good day, sir.")
            break
