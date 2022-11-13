from gtts import gTTS
from random import choice, random

text = "The red zone is for immediate loading and unloading of passengers only. There is no stopping in a white zone."


accents = ["com","com.au","co.uk","ie","co.in", "co.za"]
accent = choice(accents)
tts = gTTS(text, lang='en', tld=accent)
tts.save("main.mp3")


