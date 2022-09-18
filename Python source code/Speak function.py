#import module
import pyttsx3 

#creating a speak function 

def speak(audio): 
  engine=pyttsx3.init('sapi5')
  engine.setProperty("rate", 178)
  engine.say(audio)
  engine.runAndWait() 
  
#Running speak function
speak("hello")
