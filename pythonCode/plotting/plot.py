__author__ = 'shawn'
from plotting.lib import data
from plotting.lib import animationError
from plotting.lib import offlineAnimatedError

def plotData(w1 =0,w2 =0,dataFile = []):
    data.plotData(w1,w2,dataFile)


def animatedError(filename = "Data.txt"):
    a = animationError.animatedPlot()
    return a.plot(filename)

def offlineErrorAnimated(filename = "Data.txt", offlineDataFileName = 'offlineErrorData.txt'):
    a = offlineAnimatedError.animatedPlot()
    return a.plot(filename,offlineDataFileName)

