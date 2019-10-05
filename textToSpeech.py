from gtts import gTTs
import os
mytext='Hi Shweta! There is something Vimal wants to say you that when you are in kitchen, you are rude sometime. Be careful'

language='en'

x=gTTs(text=mytext, lang=language)
x.save("speech.mp3")

os.system("speech.mp3")
