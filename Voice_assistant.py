import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import webbrowser
import subprocess
import os

# =========================
# TEXT TO SPEECH
# =========================
def speak(text):
    print(text)
    try:
        tts = gTTS(text=text, lang="en")
        filename = "voice.mp3"
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    except Exception as e:
        print("TTS ERROR:", e)

# =========================
# SPEECH TO TEXT
# =========================
recognizer = sr.Recognizer()
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.2)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()

        except sr.WaitTimeoutError:
            return ""

        except sr.UnknownValueError:
            return ""

        except sr.RequestError:
            speak("Speech service error")
            return ""

# =========================
# COMMAND HANDLER
# =========================
def execute_command(command):

    print("COMMAND RECEIVED:", command)

    if "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "whatsapp" in command:
        speak("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")

    elif "instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    elif "facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "spotify" in command:
        speak("Opening Spotify")
        webbrowser.open("https://open.spotify.com")

    elif "notepad" in command:
        speak("Opening Notepad")
        subprocess.Popen("notepad.exe")

    elif "calculator" in command:
        speak("Opening Calculator")
        subprocess.Popen("calc.exe")

    elif "chrome" in command:
        speak("Opening Chrome")
        path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

        if os.path.exists(path):
            subprocess.Popen(path)
        else:
            speak("Chrome not found")

    elif "stop" in command or "exit" in command:
        speak("Goodbye")
        return False

    else:
        # 🔥 IMPORTANT FIX
        speak("Sorry, I don't know that command")
        print("UNKNOWN COMMAND:", command)

    return True

# =========================
# MAIN LOOP
# =========================
def main():

    speak("Voice Assistant Started. Say Jarvis to activate.")

    while True:

        command = listen()

        if not command:
            continue

        # STOP ANYTIME
        if "stop" in command or "exit" in command:
            speak("Goodbye")
            break

        # WAKE WORD SYSTEM
        if "jarvis" in command:
            speak("Yes?")

            command = listen()

            if command:
                execute_command(command)

# =========================
# RUN
# =========================
if __name__ == "__main__":
    main()