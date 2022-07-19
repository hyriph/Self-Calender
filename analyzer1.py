import ast
import datetime
from types import ModuleType

PATH = './CustomData'
LIST = []

for i in range(12):
    with open(f'{PATH}/2021-{i+1:02d}.js', 'r') as f:
        readline = f.read().split('\n')
        place = 0

        while True:
            if ('var Checks' not in readline[place]):
                place += 1
            else:
                break

        first_line = readline[place]
        first_line = first_line.replace('var', '').replace('Checks', '').replace('=', '')

        LIST.append(ast.literal_eval(first_line.lstrip()))

for MONTHNUMBER, MONTH in enumerate(LIST):
    for DAYNUMBER, DAY in enumerate(MONTH):
        DAY = DAY.split(':')
        LIST[MONTHNUMBER][DAYNUMBER] = DAY

한달에몇번 = []

for MONTH in LIST:
    # print(len(MONTH))
    한달에몇번.append(len(MONTH))

일로만보자 = []

for i in range(31):
    일로만보자.append(0)

for MONTH in LIST:
    for DAY in MONTH:
        # print(int(DAY[0]))
        일로만보자[int(DAY[0]) - 1] += 1


# for 일 in 일로만보자:
    # print(일)

요일로보자 = []

for i in range(7):
    요일로보자.append(0)

for MONTHNUMBER, MONTH in enumerate(LIST):
    for DAYNUMBER, DAY in enumerate(MONTH):
        # print(MONTHNUMBER + 1)
        # print(DAY[0])

        obj = datetime.datetime(2021, MONTHNUMBER + 1, int(DAY[0]))
        요일로보자[obj.weekday()] += 1


# for 요일 in 요일로보자:
#     print(요일)

횟수보기 = []

for i in range(3):
    횟수보기.append(0)

for MONTHNUMBER, MONTH in enumerate(LIST):
    for DAYNUMBER, DAY in enumerate(MONTH):

        횟수보기[int(DAY[1]) - 1] += 1


csv = []

for i in range(12):
    csv.append([])

onlyday = []

for i in range(12):
    onlyday.append([])

# function that returns the first item in a list of lists of LIST
for MONTHNUMBER, MONTH in enumerate(LIST):
    for DAYNUMBER, DAY in enumerate(MONTH):
        onlyday[MONTHNUMBER].append(DAY[0])

print(onlyday)

onlycount = []

for i in range(12):
    onlycount.append([])

# function that returns the first item in a list of lists of LIST
for MONTHNUMBER, MONTH in enumerate(LIST):
    for DAYNUMBER, DAY in enumerate(MONTH):
        onlycount[MONTHNUMBER].append(DAY[1])

print(onlycount)

# print(get_first_item(LIST))

for MONTH in range(0, 12):
    for DAY in range(0, 31):
        print(onlyday[MONTH])
        if str(DAY + 1) not in onlyday[MONTH]:
            print(f'{MONTH + 1}월 {DAY + 1}일은 없습니다.')
            csv[MONTH].append('0')
        else:
            print(f'{MONTH + 1}월 {DAY + 1}일은 있습니다.')
            print(onlycount[MONTH][onlyday[MONTH].index(str(DAY + 1))])
            csv[MONTH].append(onlycount[MONTH][onlyday[MONTH].index(str(DAY + 1))])
        # print(MONTH, DAY)
        pass

print(csv)

import numpy

array = numpy.asarray(csv)
numpy.savetxt('foo.csv', array, delimiter=', ', fmt='%s')