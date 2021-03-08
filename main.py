import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes
from spotify import Spotify
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

listener = sr.Recognizer()
engine = pyttsx3.init("espeak", debug=True)
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', 'english-us')

NAME = 'tony'
MIC_INDEX = 0

spotify = Spotify()


def talk(text):
    print(f"Saying: {text}")
    tts = gTTS(text=text, lang='en')
    filename = 'tts.mp3'
    tts.save(filename)

    sound = AudioSegment.from_mp3(filename)
    play(sound)


def take_command():
    try:
        with sr.Microphone() as source:
            print(source)
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if NAME in command:
                command = command.replace(NAME, '')
    except Exception as e:
        print(f"Error: {e}")

    return command


def run():
    command = take_command()
    print(command)

    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'play' in command:
        song = command.replace('play', '')
        spotify.play_song(song)
    elif 'louder' in command and 'spotify' in command:
        spotify.louder()
    elif 'next' in command:
        spotify.next_track()
    else:
        talk('Please say the command again.')


print(f"Starting {NAME}")

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    if name == "default":
        MIC_INDEX = index

print(f"Using microphone index {MIC_INDEX}")
talk(f"Starting {NAME}")

while True:
    try:
        run()
    except Exception as e:
        print(f"Failed due to {e}")

