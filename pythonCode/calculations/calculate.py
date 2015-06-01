__author__ = 'shawn'
from calculations.lib import error
from calculations.lib import offlineData
from calculations.lib import findW

def calculateError(w1, w2, data = [], display = True):
    return error.calculate(w1, w2, data, display)

# you must have a file called Data.txt where it will be your training data will be saved to. suggest using my data
# generation files in my format.
def calculateOfflineAnimationError(deltaX = 1, deltaY = -2, data = [], meshNumber = 10,iterations = 10, fileName = "offlineErrorData.txt"):
    return offlineData.calcOfflineData(deltaX, deltaY,meshNumber,iterations, fileName)

# Only works with 2 inputs to find 2 weights
def findWeights(data = [],plot = True, showError = True, epsilon = 0.1):
    return findW.find(data, plot, showError, epsilon)