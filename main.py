from json import load
from datetime import datetime
from os import get_terminal_size
import math
dayNow = datetime.today().weekday()
timeNow = datetime.now().hour * 60 + datetime.now().minute
maxLen = 0
terminalWidth = get_terminal_size().columns
tableWidth = 55
halfPadding = int((terminalWidth - tableWidth) / 2)

def check(number, data, thisDay):
    global nxtLessSwitch, dayNow, description
    pre = int(data[:2]) * 60 + int(data[3:5])
    post = int(data[8:10]) * 60 + int(data[11:13])
    if (pre <= timeNow < post and thisDay == dayNow):
        nxtLessSwitch = False
        remainingTime = int(post) - int(timeNow)
        padding = 3 if remainingTime > 59 else 6
        description = f"{formatInvert((' ' * (padding + halfPadding)) + 'Сейчас идет ')}{formatB(number)}{formatInvert(' пара. Окончание через ' + ('1 час ' if remainingTime > 59 else '') + str(remainingTime % 60) + ' мин. ' + (' ') * (padding + (1 if (remainingTime % 60 < 10) else 0) + (halfPadding if terminalWidth % 2 == 0 else halfPadding - 1)))}"
        return formatB(data)
    else:
        if (post > timeNow and nxtLessSwitch and thisDay == dayNow):
            nxtLessSwitch = False
            remainingTime = int(pre) - int(timeNow)
            description = f"{formatInvert(' ' * (halfPadding + 14))}{formatLB(number)}{formatInvert(' пара начнется через ' + str(remainingTime) + ' мин.' + (' ' * (13 + (1 if (remainingTime % 60 < 10) else 0) + (halfPadding if terminalWidth % 2 == 0 else halfPadding - 1))))}"
            return formatLB(data)
        else:
            return data

with open('/lib/calls/data-call.json', 'r', encoding='utf-8') as json_file:
    data = load(json_file)
    def formatInvert(t):
        return f'\033[{data['colors']['secondDefaultColor'][0]}m\033[{data['colors']['secondDefaultColor'][1]}m{t}\033[{data['colors']['firstDefaultColor'][0]}m\033[{data['colors']['firstDefaultColor'][1]}m'
    def formatB(t):
        return f'\033[{data['colors']['firstAccentColor'][0]}m\033[{data['colors']['firstAccentColor'][1]}m{t}\033[{data['colors']['firstDefaultColor'][0]}m\033[{data['colors']['firstDefaultColor'][1]}m'
    def formatLB(t):
        return f'\033[{data['colors']['secondAccentColor'][0]}m\033[{data['colors']['secondAccentColor'][1]}m{t}\033[{data['colors']['firstDefaultColor'][0]}m\033[{data['colors']['firstDefaultColor'][1]}m'
    if (data['clearTerminal']):
        from os import name, system
        system('cls' if name == 'nt' else 'clear')
    if (data["showTime"]):
        print('\n' + formatInvert(f"{' ' * ((round(terminalWidth / 2) - 1 if (terminalWidth % 2) == 0 else round(math.floor(terminalWidth / 2))) - 2)}{round(math.floor(timeNow / 60))}:{(timeNow % 60) if (timeNow % 60) > 9 else '0' + str((timeNow % 60))}{' ' * ((round(terminalWidth / 2) if (terminalWidth % 2) == 0 else round(math.floor(terminalWidth / 2))) - 2)}"))

    daysInfo = data['associations']
    for item in daysInfo.items():
        if dayNow in item[1]:
            dayNow = item[0]
    allStr = f"{(' ' * (terminalWidth))}{formatInvert('\n' + ' ' * (int(halfPadding)))}{formatInvert('    Понедельник   | Вторник-Пятница  |     Суббота      ')}{formatInvert(' ' * (halfPadding if terminalWidth % 2 == 0 else halfPadding - 1)) + '\n' + ('-' * terminalWidth)}\n"
    description = formatInvert(f"{' ' * (13 + halfPadding)}Нет предстоящих/нынеидущих пар{' ' * (13 + (halfPadding if terminalWidth % 2 == 0 else halfPadding - 1))}")
    for day in data['call']:
        maxLen = len(data['call'][day]) if maxLen < len(data['call'][day]) else maxLen
    days = []
    for day in data['call']:
        lessons = []
        nxtLessSwitch = True
        for l in range(0, maxLen):
            try:
                lessons.append(f"{str(l + 1)}. {check(l + 1, data['call'][day][l], day)}")
            except IndexError:
                lessons.append(' ' * 16)
        days.append(lessons)
    for l in range(0, len(days[0])):
        allStr += ' ' * halfPadding
        for d in range(0, len(days)):
            allStr += f"{(' ' if (d == 0) else '')}{days[d][l]}{((' | ') if (d != len(days) - 1) else ' ' * (halfPadding + 1 if terminalWidth % 2 == 0 else halfPadding))}"
    allStr += f"{('-' * terminalWidth)}\n{description}\n"
    print(allStr)