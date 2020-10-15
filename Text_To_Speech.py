from gtts import gTTS

import os

f = open('3.txt')
x = f.read()

language = 'en'

audio = gTTS(text=x, lang=language, slow=False)

audio.save("3.wav")
os.system("3.wav")
