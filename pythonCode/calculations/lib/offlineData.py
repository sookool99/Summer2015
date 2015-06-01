__author__ = 'shawn'
import numpy as np
import csv
from random import randint
import sys
from calculations.lib import error

def calcOfflineData(deltaX, deltaY,data, meshNumber,iterations, fileName):
    data = []
    x = np.linspace(-10,10,meshNumber)
    y = np.linspace(-10,10,meshNumber)
    x, y = np.meshgrid(x,y)
    if(isinstance(data,str) or not len(data)):
        if not len(data):
            data = 'Data.txt'
        with open('dataFiles/' + data) as fp:
            reader = csv.reader(fp, delimiter=',')
            for line in reader:
                data.append([int(line[0]), float(line[1]), float(line[2])])

    changingIndex = randint(0,len(data) -1)

    dataFile = open(fileName, "w")
    writer = csv.writer(dataFile, delimiter=',')
    writer.writerow([deltaX, deltaY,changingIndex, iterations, meshNumber])

    for i in range(0,iterations):
        print("On Iteration %d of moving points"%i)
        sys.stdout.flush()
        data[changingIndex][1] += deltaX
        data[changingIndex][2] += deltaY
        if data[changingIndex][1] < -10:
            deltaX *= -1
        if data[changingIndex][1] > 10:
            deltaX *= -1
        if data[changingIndex][2] < -10:
            deltaY *= -1
        if data[changingIndex][2] > 10:
            deltaY *= -1
        counter = 0
        totalIter = meshNumber**2
        print("Done(out of %d):"%totalIter, end="")
        zData = []
        for X,Y in zip(np.ravel(x), np.ravel(y)):
            zData.extend([error.calculateError(X,Y, data,False)])
            if counter % int((totalIter / 10)) == 0:
                print(" %d"%counter, end="")
            counter += 1
        z = np.array(zData)
        print('\n', end="")
        writer.writerow(z)
    dataFile.close()
    print("Done Offline Calculations!")