from json import load
from datetime import datetime
from os import system, get_terminal_size
dayNow = datetime.today().weekday()
daysInfo = { 'p': [1], 'v': [2, 3, 4, 5], 's': [6] }
for item in daysInfo.items():
    if dayNow in item[1]:
        dayNow = item[0]
timeNow = datetime.now().hour * 60 + datetime.now().minute
maxLen = 0
terminalWidth = get_terminal_size().columns
tableWidth = 55
halfPadding = int((terminalWidth - tableWidth) / 2)
system('clear')

def formatInvert(t):
    return f'\033[30m\033[47m{t}\033[0m'
def formatB(t):
    return f'\033[44m{t}\033[0m'
def formatLB(t):
    return f'\033[46m{t}\033[0m'

def check(number, data, thisDay):
    global nxtLessSwitch, dayNow, description
    pre = int(data[:2]) * 60 + int(data[3:5])
    post = int(data[8:10]) * 60 + int(data[11:13])
    if (pre <= timeNow < post and thisDay == dayNow):
        nxtLessSwitch = False
        remainingTime = int(post) - int(timeNow)
        padding = 3 if remainingTime > 59 else 6
        description = f"{formatInvert((' ' * (padding + halfPadding)) + 'Сейчас идет ')}{formatB(number)}{formatInvert(' пара. Окончание через ' + ('1 час ' if remainingTime > 59 else '') + str(remainingTime % 60) + ' мин. ' + (' ') * (padding + (1 if (remainingTime % 60 < 9) else 0) + (halfPadding if terminalWidth % 2 == 0 else halfPadding - 1)))}"
        return formatB(data)
    else:
        if (post > timeNow and nxtLessSwitch and thisDay == dayNow):
            nxtLessSwitch = False
            remainingTime = int(pre) - int(timeNow)
            description = f"{formatInvert(' ' * (halfPadding + 14))}{formatLB(number)}{formatInvert(' пара начнется через ' + str(remainingTime) + ' мин.' + (' ' * (13 + (1 if (remainingTime % 60 < 9) else 0) + (halfPadding if terminalWidth % 2 == 0 else halfPadding - 1))))}"
            return formatLB(data)
        else:
            return data


with open('data-call.json') as json_file:
    data = load(json_file)
    allStr = f"{(' ' * 55)}{formatInvert('\n' + ' ' * (int(halfPadding)))}{formatInvert('    Понедельник   | Вторник-Пятница  |     Суббота      ')}{formatInvert(' ' * (halfPadding if terminalWidth % 2 == 0 else halfPadding - 1)) + '\n' + ('-' * terminalWidth)}\n"
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
            allStr += f"{(' ' if (d == 0) else '')}{days[d][l]}{((' | ') if (d != len(days) - 1) else '\n')}"
    allStr += f"{('-' * terminalWidth)}\n{description}\n"
    print(allStr)