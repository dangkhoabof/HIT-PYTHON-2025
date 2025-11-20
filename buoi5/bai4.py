def create_event(name, day, time):
    return {"name": name, "day": day, "time": time}

def add_event(schedule, event):
    schedule.append(event)

def find_by_day(schedule, day):
    return [e for e in schedule if e["day"].lower() == day.lower()]


def remove_event(schedule, name):
    for i in range(len(schedule)):
        if schedule[i]["name"] == name:
            schedule.pop(i)
            return True
    return False


def export_schedule(schedule):
    lines = []
    for event in schedule:
        day = event["day"]
        time = event["time"]
        name = event["name"]
        lines.append(f"{day} {time} - {name}")
    return "\n".join(lines)

schedule = []
add_event(schedule, create_event("Physics", "Tuesday", "09:00"))
print(export_schedule(schedule))
