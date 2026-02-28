
# Simple Text-to-Speech Program using pyttsx3

# This script initializes a text-to-speech engine
# and converts a given text string into spoken audio output.


import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Provide the text that should be spoken
engine.say("My name is Vishakha")

# Execute the speech command and wait until completion
engine.runAndWait()
