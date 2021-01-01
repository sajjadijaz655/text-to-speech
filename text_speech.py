from gtts import gTTS
import os

mytext="Sajjad is a good Boy"

lan="en"

output=gTTS(text=mytext,lang=lan,slow=False)

output.save("speech.mp3")

os.system("start speech.mp3")




