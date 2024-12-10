from json import load
from datetime import datetime
from os import get_terminal_size, getcwdb, path
import math, sys
from time import sleep

maxLen = 0
tableWidth = 55
nl = '\n'


currentDir = path.dirname(path.realpath(__file__))

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

with open(f"{currentDir}/data-call.json", 'r', encoding='utf-8') as json_file:
    data = load(json_file)
    if (data['clearTerminal']):
            from os import name, system
    def getColor(color):
        if len(data['colors'][color]) == 0:
            return '\033[0m'
        retStr = ''
        for item in data['colors'][color]:
            try:
                item = int(item)
                if (item == 0 or (30 <= item <= 37) or ((40 <= item <= 47))):
                    retStr += f'\033[{item}m'
                else:
                    retStr += '\033[0m'
                    break
            except:
                retStr += '\033[0m'
                break
        return retStr 

    def formatInvert(t):            
        return f"{getColor('secondDefaultColor')}{t}{getColor('firstDefaultColor')}"
    def formatB(t):
        return f"{getColor('firstAccentColor')}{t}{getColor('firstDefaultColor')}"
    def formatLB(t):
        return f"{getColor('secondAccentColor')}{t}{getColor('firstDefaultColor')}"


    def iteration():
            global maxLen, tableWidth, timeNow, dayNow, halfPadding, terminalWidth, description, iterator, nxtLessSwitch
            if (data['clearTerminal']):
                system('cls' if name == 'nt' else 'clear')
            dayNow = datetime.today().weekday()
            terminalWidth = get_terminal_size().columns
            sec = str(datetime.now().second) if datetime.now().second > 9 else str(0) + str(datetime.now().second)
            min = str(datetime.now().minute) if datetime.now().minute > 9 else str(0) + str(datetime.now().minute)
            hrs = str(datetime.now().hour) if datetime.now().hour > 9 else str(0) + str(datetime.now().hour)
            timeNow = int(hrs) * 60 + int(min)
            if (data['time']['clock']):
                iterator = not iterator
            

            if (data["time"]["show"]):
                time = ''
                if (data['time']['preset']['hrs']):
                    time += hrs + (':' if (iterator) else ' ')
                if (data['time']['preset']['min']):
                    time += min
                if (data['time']['preset']['sec']):
                    time += (':' if (iterator) else ' ') + sec
                timePadCounter = math.floor((terminalWidth / 2) - (len(time) / 2))
                print(nl + formatInvert(str(' ' * timePadCounter) + time + (' ' * (timePadCounter if (terminalWidth == timePadCounter * 2 + len(time)) else timePadCounter + 1))))

            halfPadding = int((terminalWidth - tableWidth) / 2)

            daysInfo = data['associations']
            for item in daysInfo.items():
                if dayNow in item[1]:
                    dayNow = item[0]
            allStr = f"{(' ' * (terminalWidth))}{formatInvert(nl + ' ' * (int(halfPadding)))}{formatInvert('    Понедельник   | Вторник-Пятница  |     Суббота      ')}{formatInvert(' ' * (halfPadding if terminalWidth % 2 == 0 else halfPadding - 1)) + nl + ('-' * terminalWidth)}{nl}"
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
            if (data["flowMode"]):
                print('press Enter to stop')


    iterator = True

    def loop(done, interval=data['updateTime']):
        while not done.wait(interval):
            iteration()
        
    if (data["flowMode"]):
        iteration()
        from threading import Event, Thread
        done = Event()
        Thread(target=loop, args=[done], daemon=True).start()
        input()
        done.set()
        system('cls' if name == 'nt' else 'clear')
        
    else:
        iteration()