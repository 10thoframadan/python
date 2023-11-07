import win32com.client as win32com

speak = win32com.Dispatch("SAPI.SpVoice")
print("Welcome to Robo Speaker")

while True:
  userInp = input("What you want to speak (type \"00\" to exit)\n: ")
  if userInp == "00":
    speak.Speak("Bye Bye!")
    print("Thanks for using Robo Speaker")
    break
  else:
    command = speak.Speak(userInp)
