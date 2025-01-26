import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

def speak(text):
    """Make the assistant speak"""
    engine.say(text)
    engine.runAndWait()
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
      speak("I am listening,please speak.")
      try:
        audio = recognizer.listen(source)
        command = recogizer.recognizer_google(audio)
        return command.lower()
      except sr.UnknownValueError:
        speak("Sorry, I did not catch that")
        return ""
def main():
  speak('Hello! Iam your simple bot from Mallareddy college')
  speak('you can say hello, ask my name or say goodbye')
  while True:
    command = input('You: ').lower()
    if 'hello' in command:
      speak('Hello! Welcome to Mallareddy college')
    elif 'what is your name' in command :
      speak('you can say hello, ask my name or say goodbye')
    elif 'goodbye' in command:
      speak("Goodbye! Have a nice day")
      break
    else:
      speak('I dont understand that. Please try again')

if __name__ == '__main__':
  main()