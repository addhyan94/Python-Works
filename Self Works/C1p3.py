# Install an external module and use it to perform an operating of your interest.

import pyttsx3

engine = pyttsx3.init()
engine.say("I will speak this text ")
engine.runAndWait()