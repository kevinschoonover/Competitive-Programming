'''
Programmer:,Kevin Schoonover
Start Date: 2016/09/03
End Date:
Program: Daylight Saving Time (https://open.kattis.com/problems/dst)
'''
from math import floor
import sys

def DSTCalculator(direction, changeMinutes, currentHour, currentMinute):
    minuteTime= int(currentHour)*60 + currentMinute
    if direction == "B":
        minuteTime -= changeMinutes
        if minuteTime < 0:
            minuteTime = 24*60 + minuteTime
        ConvertTime(minuteTime)
    elif direction == "F":
        minuteTime += changeMinutes
        if minuteTime > 1440:
            minuteTime -= 1440
    hours, minutes = ConvertTime(minuteTime)
    print(hours,minutes)


def ConvertTime(minuteTime):
    hours = int(floor(minuteTime/60))
    minutes = minuteTime - hours * 60
    return hours,minutes

with open("test.txt", 'r') as f:
    index = int(f.readline())
    for i in range(index):
        inputList = f.readline()
        inputList.replace(" ","").split(',')
        print(i,":",inputList[3])
