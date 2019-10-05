from gtts import gTTS
import os
mytext='''hello shweta pandey. Vimal loves you. do you know that?
good night.'''

language='en'

x=gTTS(text=mytext, lang=language, slow=True)
x.save("speech.mp3")

os.system("speech.mp3")
