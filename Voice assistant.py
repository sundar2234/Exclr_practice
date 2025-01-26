import pyttsx3

engine = pyttsx3.init()
def speak(text):
  """Make assistance speak"""
  engine.say(text)
  engine.runAndWait()

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