'''
Programmer:Kevin Schoonover
Start Date: 2016/09/04
End Date:
Program: 12791 - Lap (https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=823&page=show_problem&problem=4656)
'''

def OverlapCalculator(timea, timeb):
    laps = 0
    DELTATIME = timeb-timea
    deltaLap = 0
    while deltaLap < timeb:
        deltaLap += DELTATIME
        laps += 1
    print(laps)
