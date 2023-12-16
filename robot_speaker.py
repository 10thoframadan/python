import win32com.client as win32com

speak = win32com.Dispatch("SAPI.SpVoice")

while True:
    user_input = input("What you want to speak (type \"00\" to exit)\n: ")
    if user_input == "00":
        speak.Speak("Disconnected.")
        break
    else:
        command = speak.Speak(user_input)
