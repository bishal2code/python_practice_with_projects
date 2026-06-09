logs = [
    "2026-10-12 Error Storage Full",
    "2025-01-23 Error Ram Full",
    "2024-02-12 Info Charge Device"
]

entries = [tuple(line.split(" ",2)) for line in logs]

logCounter = {}

for _, level, _ in entries:
    logCounter[level] = logCounter.get(level, 0) + 1


uniqueMessage = {msg for _, _, msg in entries}

print("Log Counts", logCounter)
print("Unique Message", uniqueMessage)