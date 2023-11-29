import win32com.client as win32com

speak = win32com.Dispatch("SAPI.SpVoice")
print("\n---- Welcome to robo speaker ----")

while True:
  admin = input("What you want to speak (type \"00\" to exit)\n: ")
  if admin == "00":
    speak.Speak("Goodbye.")
    print("Thanks for using robo speaker")
    break
  else:
    command = speak.Speak(admin)
