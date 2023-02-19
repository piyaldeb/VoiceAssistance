import datetime
import pyttsx3
import speech_recognition as sp
import webbrowser
import pyjokes
import pyaudio


def stotext():
    recognize = sp.Recognizer()
    with sp.Microphone() as source:
        print("Listening")
        recognize.adjust_for_ambient_noise(source)
        audio = recognize.listen(source)
        try:
            print("Recognizing")
            data = recognize.recognize_google(audio)
            return data
        except sp.UnknownValueError:
            print("Not Understand")


def texttospech(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 130)
    engine.say(x)
    engine.runAndWait()


if __name__ == '__main__':

    data = stotext().lower()
    if "your name" in data:
        name = "my name is Hexa"
        texttospech(name)
    elif "time" in data:
        time = datetime.datetime.now().strftime("%I%M%p")
        texttospech(time)

    elif "youtube" in data:
        webbrowser.open("https://www.youtube.com/")

    else:
        try:

            url = f"https://www.google.com/search?q={data}"

            webbrowser.open(url)  # Open the URL in the default web browser
        except:
            print("Sorry, could not recognize your voice.")

