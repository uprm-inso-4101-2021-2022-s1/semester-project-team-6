from .models import Event

def generateCalendarEntries(id):
    events = Event.objects.filter(student = id)

    result = ""

    for i in range(len(events)):
        result += '{id: ' + str(i) + ',name: "' + events[i].name + '", start: "' + str(events[i].date) + 'T00:00:00", end: "' + str(events[i].date) + 'T00:00:00"},'

    return result

def getBuildingCode(room):
    room = room.upper()

    if(room[0].isalpha() and room[1].isalpha()):
        return room[0] + room[1]
    elif(room[0].isalpha()):
        return room[0]
    else:
        return "unknown"
