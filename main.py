from gtts import gTTS
from random import choice
from pygame import mixer
# from playsound import playsound
from time import sleep

text = "The red zone is for immediate loading and unloading of passengers only. There is no stopping in a white zone."
slow = False

accents = ["com", "com.au", "co.uk", "ie", "co.in", "co.za"]
accent = choice(accents)

tts = gTTS(text, tld=accent, slow=slow)
tts.save("main.mp3")


mixer.init()
mixer.music.load("main.mp3")
mixer.music.play()
while mixer.music.get_busy() == True:
    continue
# playsound('main.mp3')
sleep(3)
