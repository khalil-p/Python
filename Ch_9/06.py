

with open("log.txt") as f:
    log = f.read()

if "python" in log.lower():
    print("Log file contain python")
else:
    print("Log file does not contain python")
