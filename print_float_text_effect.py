import time

def print_float_text_effect(text, delay=0.05):
  for char in  text:
    print(char, end='', flush=True)
    time.sleep(delay)
  print()

print_float_text_effect("Hi, I am a Mohamed Abdel Rahman")
time.sleep(1)
print_float_text_effect("I am a python programming student")
time.sleep(1)
print_float_text_effect("When I want use a print effect I use this program")
time.sleep(1)
print("Follow me on instagram @8ouc for anyHelp...")
time.sleep(1)
