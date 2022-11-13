from gtts import gTTS
from random import choice, random
from playsound import playsound

text = "The red zone is for immediate loading and unloading of passengers only. There is no stopping in a white zone."
slow = False

accents = ["com", "com.au", "co.uk", "ie", "co.in", "co.za"]
accent = choice(accents)

tts = gTTS(text, lang='en', tld=accent, slow=slow)
tts.save("main.mp3")


playsound('main.mp3')
