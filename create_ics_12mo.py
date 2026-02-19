#!/usr/bin/env python3
import json
from icalendar import Calendar, Event
from datetime import datetime, timedelta
import sys
import os

# Output ICS path in repo root
ics_path = os.path.expanduser("~/UKBinCollectionData/south-norfolk-bins.ics")

# Load JSON from stdin
data = json.load(sys.stdin)

cal = Calendar()
cal.add('prodid', '-//South Norfolk Bin Collection//')
cal.add('version', '2.0')

name_map = {
    "RefuseBin": "Black Bin",
    "RecycleBin": "Recycling",
    "GardenBin": "Garden Waste"
}

intervals = {
    "RefuseBin": 2,
    "RecycleBin": 3,
    "GardenBin": 2
}

for bin_item in data['bins']:
    event = Event()
    dt = datetime.strptime(bin_item['collectionDate'], "%d/%m/%Y")
    event.add('summary', name_map.get(bin_item['type'], bin_item['type']))
    event.add('dtstart', dt.date())
    event.add('dtend', dt.date())
    event.add('dtstamp', datetime.now())

    interval = intervals.get(bin_item['type'], 2)
    event.add('rrule', {
        'freq': 'weekly',
        'interval': interval,
        'until': (dt + timedelta(weeks=52)).date()
    })

    cal.add_component(event)

with open(ics_path, 'wb') as f:
    f.write(cal.to_ical())

print(f"ICS created at {ics_path}")