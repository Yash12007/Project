print("Make sure you are using pc or laptop with the given libraries.")
print("commands for shell:")
print("pip install speech_recognition")
print("pip install pyaudio")
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:                
  # use the default microphone as the audio source
    audio = r.listen(source)                  
  # listen for the first phrase and extract it into audio data

try:
    print("You said " + r.recognize(audio))    # recognize speech using Google Speech Recognition
  
except LookupError:                           # speech is unintelligible
    print("Could not understand audio")

if r.recognize["value"]==1:
  print("mic on")
else:
  print("mic off")