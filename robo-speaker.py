import win32com.client as win32com

speak = win32com.Dispatch("SAPI.SpVoice")
print("Welcome to robo speaker")

while True:
  userInp = input("What you want to speak (type \"00\" to exit)\n: ")
  if userInp == "00":
    speak.Speak("Goodbye.")
    print("Thanks for using robo speaker")
    break
  else:
    command = speak.Speak(userInp)
