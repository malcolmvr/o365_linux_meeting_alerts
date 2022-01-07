from datetime import datetime, timedelta, timezone
from update_ui import show_imminent_event

with open("events.txt", "r") as f:
    event_times = [datetime.fromisoformat(stime) for stime in f.read().split("\n")]

now = datetime.now(timezone.utc)
imminent_events = [
    ev for ev in event_times
    if ev > now and ev < (now + timedelta(minutes=5))
]

show_imminent_event(bool(imminent_events))
