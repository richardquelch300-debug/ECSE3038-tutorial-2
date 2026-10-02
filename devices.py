readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]


def list_devices(devices):
    for device in devices:
        print(device["name"], device["temp"])


list_devices(readings)



def average_temp(devices):
    total = 0
    for device in devices:
        total += device["temp"]
    return total / len(devices)

print(average_temp(readings))



def hottest(devices):
    best = devices[0]
    for device in devices:
        if device["temp"] > best["temp"]:
            best = device
    return best

print(hottest(readings))



def to_status(device):
    return {
        "device": device["name"],
        "status": "ok" if device["online"] else "offline",
        "celsius": device["temp"],
    }

print(to_status(readings[3]))



def by_room(devices):
    rooms = {}
    for device in devices:
        room = device["room"]
        if room not in rooms:
            rooms[room] = []
        rooms[room].append(device["name"])
    return rooms


print(by_room(readings))