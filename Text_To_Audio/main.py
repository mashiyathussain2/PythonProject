from gtts import gTTS
from playsound import playsound

audio = 'saveaudio.mp3'
language = input("Enter lanuage: ")
sp = gTTS(text = input("Enter text: "), lang = language, slow=False)
sp.save(audio)
playsound(audio)
