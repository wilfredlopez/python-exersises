

DAYS_SWITCH = {"monday": 'tuesday',
               'tuesday': 'wednesday',
               'wednesday': 'thursday',
               'thursday': 'friday',
               'friday': 'saturday',
               'saturday': 'sunday',
               'sunday': 'monday'}


def get_is_am(amorpm):
    return str(amorpm).lower() == 'am'


def pretty_print(value):
    if(len(str(value)) == 1):
        return "0"+str(value)
    else:
        return str(value)


def add_day(day):
    return DAYS_SWITCH[str(day).lower()]


def pretty_print_day(day):
    return str(day[0]).upper() + str(day[1:]).lower()


def print_days_diff(elapsedDays: int):
    if elapsedDays == 1:
        return '(next day)'
    else:
        return '({0} days later)'.format(elapsedDays)


def switchAmPm(current):
    isAm = get_is_am(current)
    if isAm:
        return "PM"
    else:
        return "AM"


def add_time(start, duration, day=None):
    '''
@params start: a start time in the 12-hour clock format (ending in AM or PM)
@params duration: a duration time that indicates the number of hours and minutes
@param day: (optional) a starting day of the week, case insensitive
'''

    # data gather
    hour = int(start.split(':')[0])
    minutes = int(start.split(":")[1].split(" ")[0])
    AM_Or_PM = start.split(":")[1].split(' ')[1]
    isAm = get_is_am(AM_Or_PM)
    durationHours = int(duration.split(':')[0])
    durationMinutes = int(duration.split(':')[1])

    # calculations
    total_seconds = ((hour + durationHours) * 3600) + \
        ((minutes + durationMinutes) * 60)
    totalHours = int((total_seconds % 86400) / 3600)
    rawDays = total_seconds / 86400
    totalMinutes = int(((total_seconds % 86400) % 3600) / 60)
    # ssss = int(((total_seconds % 86400) % 3600) % 60)
    totalDays = int(rawDays)

    shouldSwitch = not isAm
    while totalHours > 12:
        diff = totalHours - 12
        totalHours = diff
        AM_Or_PM = switchAmPm(AM_Or_PM)
        if shouldSwitch:
            totalDays = totalDays + 1
            shouldSwitch = False
        else:
            shouldSwitch = True

    if totalHours == 12 and not isAm:
        totalDays = totalDays + 1
        AM_Or_PM = switchAmPm(AM_Or_PM)

    if totalHours == 12 and isAm:
        AM_Or_PM = switchAmPm(AM_Or_PM)

    for x in range(totalDays):
        if day is not None:
            day = add_day(day)

    result = str(totalHours) + ":" + \
        pretty_print(totalMinutes) + " "+AM_Or_PM
    if day is not None:
        result += ", " + pretty_print_day(day)
    if totalDays > 0:
        result += " " + print_days_diff(totalDays)
    return result


# add_time("3:00 PM", "3:10")
# # Returns: 6:10 PM

# add_time("11:30 AM", "2:32", "Monday")
# # Returns: 2:02 PM, Monday

# add_time("11:43 AM", "00:20")
# # Returns: 12:03 PM

# add_time("10:10 PM", "3:30")
# # Returns: 1:40 AM (next day)

# add_time("11:43 PM", "24:20", "tueSday")
# # Returns: 12:03 AM, Thursday (2 days later)

# add_time("6:30 PM", "205:12")
# # Returns: 7:42 AM (9 days later)


# actual = add_time("11:59 PM", "24:05", "Wednesday")
# expected = "12:04 AM, Friday (2 days later)"

# print(actual)
# print(expected)
# print(actual == expected)

# print("*********************************************************")

# actual = add_time("2:59 AM", "24:00", "saturDay")
# expected = "2:59 AM, Sunday (next day)"

# print(actual)
# print(expected)
# print(actual == expected)
# print("*********************************************************")
# actual = add_time("3:30 PM", "2:12")
# expected = "5:42 PM"
# print(actual)
# print(expected)
# print(actual == expected)
# print("*********************************************************")

# actual = add_time("11:55 AM", "3:12")
# expected = "3:07 PM"
# print(actual)
# print(expected)
# print(actual == expected)
# print("*********************************************************")

# actual = add_time("2:59 AM", "24:00")
# expected = "2:59 AM (next day)"
# print(actual)
# print(expected)
# print(actual == expected)

# print("*********************************************************")

# actual = add_time("8:16 PM", "466:02")
# expected = "6:18 AM (20 days later)"
# print(actual)
# print(expected)
# print(actual == expected)

# print("*********************************************************")

# actual = add_time("11:40 AM", "0:25")
# expected = "12:05 PM"

# print(actual)
# print(expected)
# print(actual == expected)
