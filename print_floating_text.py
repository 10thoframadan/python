import time

def mohamed(text):
  for char in text:
    print(char, end='', flush=True)
    time.sleep(0.05)
  print()

mohamed("Hello world")
time.sleep(1)
mohamed("Goodbye world")
time.sleep(1)
print("Successfully...")
