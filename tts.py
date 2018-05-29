#!/usr/bin/env python3
from gtts import gTTS
import os

#to convert text to speech
def convert_text_n_speak(textInput):
	#converting text
	tts = gTTS(text=textInput, lang='en')
	#saving audio to file
	tts.save("query.wav")
	#playing audio
	os.system("mpg321 query.wav")