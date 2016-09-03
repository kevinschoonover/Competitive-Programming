'''
Programmer: Kevin Schoonover
Date: 2016/9/1
Program: Happy Happy Prime Prime (https://open.kattis.com/contests/na15warmup5/problems/happyprime)
'''
import sys
from math import fabs


'''initialRange = sys.stdin.readline()
for i in range(1,initialRange, 1):
    inputs = int(test.readline().strip("\n").replace(" ",""))
    if isPrime(inputs[1]):
        HappyLittlePrime(inputs[0],inputs[1],inital=inputs[1])
    else:
        if len(inputs) != 1:
            print(printinputs[0],inputs[1],"NO")'''
def HappyLittlePrime(index, prime, total = 0, initial= 0):
    try:
        digits = [int(i)**2 for i in str(prime)]
        for number in digits:
            total = total + int(number)
        if total != 1:
            HappyLittlePrime(index, total, initial=initial)
        else:
            print(index, initial, "YES")
    except RecursionError:
        print (index, initial, "NO")

def isPrime(num):
    testInt = [2,3,4,5,6,7,8,9]
    primeList = [2,3,5,7,11]
    if num in primeList:
        return True
    elif num == 1:
        return False
    for n in testInt:
        if num % n == 0:
            return False
    else:
        return

HappyLittlePrime(1,383, initial=383)
