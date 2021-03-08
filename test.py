from gtts import gTTS
import pyglet
import time

tts = gTTS(text='Hello World!', lang='en')
filename = 'tts.mp3'
tts.save(filename)
music = pyglet.media.load(filename, streaming=False)
music.play()
time.sleep(music.duration)
