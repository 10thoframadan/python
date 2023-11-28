import win32com.client as win32com

speak = win32com.Dispatch("SAPI.SpVoice")
print("\n---- Robot Speaker ----")
print("Welcome to robo speaker")

while True:
  user = input("What you want to speak (type \"00\" to exit)\n: ")
  if user == "00" :
    speak.Speak("Goodbye.")
    print("Thanks for using robo speaker")
    break
else:
  command = speak.Speak(user)
