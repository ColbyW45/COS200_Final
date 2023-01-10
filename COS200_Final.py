import rhinoscriptsyntax as rhino
from random import random

def generateMatrix(xMax, yMax, zMax, showPt = True):
    ptMatrix = {}

    for z in range(zMax):
        for y in range(yMax):
            for x in range(xMax):
                ptMatrix[(x, y, z)] = (x * 8, y * 8, z * 8)
                
    if showPt:
        rhino.AddPoints(list(ptMatrix.values()))
    
    return ptMatrix

def createElevation(ptMatrix):
    for pt in ptMatrix:
        rhino.MoveObject(pt, 3)

def main():
    xMax = 15
    yMax = 15
    zMax = 1

    ptMetrix = generateMatrix(xMax, yMax, zMax)
    createElevation(ptMetrix)

main()