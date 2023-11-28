import time

def print_floating_text(text):
  for char in text:
    print(char, end='', flush=True)
    time.sleep(0.05)
  print()

print_floating_text("Hi, I am a Mohamed Abdel Rahman")
time.sleep(1)
print_floating_text("I am a computer sience")
time.sleep(1)
print_floating_text("I know python programming")
time.sleep(1)
print_floating_text("Learning C C++ C#")
time.sleep(1)
print("Successfully printed floating text effect...")
