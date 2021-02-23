from gtts import gTTS
from playsound import playsound

language = 'de'
tts = gTTS(text="Hallo Welt, abonnier mich!",
           lang=language,
           slow=False)
tts.save("audio/tts.mp3")
playsound("audio/tts.mp3")