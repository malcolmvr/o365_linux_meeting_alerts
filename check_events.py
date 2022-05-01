from datetime import datetime, timedelta, timezone
from os import getenv, path
from update_ui import show_imminent_event

IS_IMMINENT_FILE = "is_imminent.txt"

with open("events.txt", "r") as f:
    event_times = [datetime.fromisoformat(stime) for stime in f.read().split("\n")]

now = datetime.now(timezone.utc)
imminent_events = [
    ev for ev in event_times
    if ev > now and ev < (now + timedelta(minutes=int(getenv("IMMINENT_MINUTES"))))
]

was_imminent = False
if path.isfile(IS_IMMINENT_FILE):
    with open(IS_IMMINENT_FILE, "r", encoding="utf-8") as f:
        contents = f.read()
        was_imminent = contents == "True"
print("was_imminent", was_imminent)

is_imminent = bool(imminent_events)

with open(IS_IMMINENT_FILE, "w", encoding="utf-8") as f:
    f.write(str(is_imminent))

show_imminent_event(was_imminent, is_imminent)
