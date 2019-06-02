import json
from helpers import to_time, pairs
from operator import itemgetter

rasp = """{
    "sunday": [
        {"type": "open", "value": 64800}
    ],
    "monday": [
        {"type": "close", "value": 24800}
    ]
}
"""


class OpeningHours:
    # Have to process Monday twice in case if Sunday not closed until midnight
    days_to_process = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "monday"]

    def __init__(self, json_str):
        self.processed_days = {}
        self.source = json.loads(json_str)
        closed = True
        prev_day = None
        for day in self.days_to_process:
            if day in self.source:
                times = sorted(self.source[day], key=itemgetter("value"))
                # Close previous day if needed
                if times and times[0]["type"] == "close":
                    if prev_day and not closed:
                        prev_day.append(times[0]["value"])
                        closed = True
                    times = times[1:]

                # Process current day
                if day not in self.processed_days:
                    processed_day = []
                    self.processed_days[day] = processed_day
                    for event in times:
                        if closed and event["type"] == "open" or \
                                not closed and event["type"] == "close":
                            processed_day.append(event["value"])
                            closed = not closed
                        else:
                            raise Exception("Wrong input data!")
                    prev_day = processed_day

    def __str__(self):
        lines = []
        for day, times in self.processed_days.items():
            line = day.capitalize() + ': '
            if times:
                schedule = ", ".join("%s - %s" % (to_time(opened), to_time(closed)) for opened, closed in pairs(times))
            else:
                schedule = "Closed"
            lines.append(line + schedule)
        return '\n'.join(lines)


print(OpeningHours(rasp))
