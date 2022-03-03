from gtts import gTTS
import os
import codecs
fname=input("Enter file name:")
var=open(fname)
with codecs.open(fname, encoding='utf-8') as f:
    tixt=f.read()
language=input("Enter the language:")#english 
obj=gTTS(text=tixt,lang=language,slow=False)#slow=false for speeding up of audio
obj.save("speech.mp3")
os.system("speech.mp3")#to open audio file automatically
