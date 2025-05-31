# Enhanced Voice Assistant in Python (App-like Behavior)
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import requests
import json

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()

def get_weather(city):
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    data = response.json()
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        description = weather["description"]
        return f"The temperature in {city} is {temperature}°C with {description}."
    else:
        return "City not found."

def run_voice_assistant():
    speak("Hello! I am your assistant. How can I help you?")

    while True:
        query = take_command()

        if 'time' in query:
            time_str = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time_str}")

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")

        elif 'play music' in query:
            music_dir = "C:\\Users\\Public\\Music"  # Change to your music folder
            songs = os.listdir(music_dir)
            if songs:
                os.startfile(os.path.join(music_dir, songs[0]))
                speak("Playing music")
            else:
                speak("No music files found")

        elif 'weather in' in query:
            city = query.split("in")[-1].strip()
            weather_info = get_weather(city)
            speak(weather_info)

        elif 'stop' in query or 'exit' in query or 'bye' in query:
            speak("Goodbye!")
            break

        else:
            speak("I didn't understand that. Please try again.")

if __name__ == "__main__":
    run_voice_assistant()
