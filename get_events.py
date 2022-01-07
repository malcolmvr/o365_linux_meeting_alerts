from datetime import datetime
from os import getenv
from os.path import isfile
from dotenv import load_dotenv
from O365 import Account

load_dotenv()

credentials = (getenv('APPLICATION_ID'), getenv('CLIENT_SECRET'))

account = Account(credentials, auth_flow_type='authorization', tenant_id=getenv('TENANT_ID'))
if not isfile("./o365_token.txt"):
    if account.authenticate(scopes=['https://graph.microsoft.com/.default', 'offline_access']):
        print('Authenticated!')
else:
    account.connection.refresh_token()

schedule = account.schedule()
calendar = schedule.get_default_calendar()

now = datetime.now()
date_query = calendar \
    .new_query('start') \
    .greater_equal(datetime(now.year, now.month, now.day, 0, 0, 0)) \
    .chain('and') \
    .on_attribute('end') \
    .less_equal(datetime(now.year, now.month, now.day, 23, 59, 59))

events = list(calendar.get_events(query=date_query, include_recurring=True))

with open("events.txt", "w") as f:
    f.write("\n".join([event.start.isoformat() for event in events]))

