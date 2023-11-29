import psutil
import time
current_processes = [(p.name(), p.pid) for p in psutil.process_iter()]
print("Current processes:")
for process, pid in current_processes:
  print(f"{process} (PID: {pid})")

while True:
  time.sleep(5)
  updated_processes = [(p.name(), p.pid) for p in psutil.process_iter()]
  new_processes = [(p, pid) for p, pid in updated_processes if p not in [p for p, _ in current_processes]]
  if new_processes:
    print("\nNew processes started:")
    for process, pid in new_processes:
      print(f"{process} (PID: {pid})")

  stopped_processes = [(p, pid) for p, pid in current_processes if p not in [p for p, _ in updated_processes]]
  if stopped_processes:
    print("\nProcesses stopped:")
    for process, pid in stopped_processes:
      print(f"{process} (PID: {pid})")

  current_processes = updated_processes
