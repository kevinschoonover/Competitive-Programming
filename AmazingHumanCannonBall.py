'''
Programmer:Kevin Schoonover
Start Date: 2016/09/03
End Date: 2016/09/03
Program: The Amazing Human Cannonball (https://open.kattis.com/problems/humancannonball2)
'''
import math;

def EvaluateTrajectory(velocity, theta, distance, lowWall, tallWall ):
    GRAVITY = 9.81
    theta = math.radians(theta)
    timeToWall = (distance/(velocity * math.cos(theta)))
    yPosition = (velocity * timeToWall * math.sin(theta)) - (1/2 * GRAVITY * (timeToWall**2))
    if yPosition > (lowWall+1) and yPosition < (tallWall-1):
        print("SAFE")
    else:
        print("NOT SAFE")
