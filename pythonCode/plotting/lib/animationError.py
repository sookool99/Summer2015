__author__ = 'shawn'
__author__ = 'shawn'
from calculations import calculate
from data import dataSuite
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator
import matplotlib.animation as animation
import csv
from random import randint

# used to genereate range of values for w1 and w2
def generateGraphData(numberOfEach):
    x = np.linspace(-10,10,numberOfEach)
    y = np.linspace(-10,10,numberOfEach)
    x, y = np.meshgrid(x,y)
    return [x,y]

# used to generate a gride and then calculate the error
def plotErrorSurface(numberOfEach = 20, data = []):
    dataPoints = generateGraphData(numberOfEach)
    xHolder = dataPoints[0]
    yHolder = dataPoints[1]
    z = np.array([calculate.calculateError(x,y, data,False) for x,y in zip(np.ravel(xHolder), np.ravel(yHolder))])
    Z = z.reshape(xHolder.shape)
    dataPoints.extend([Z])
    return dataPoints

class animatedPlot:
    iterations = 0
    deltaX = 1
    deltaY = -2
    data = []
    ax = ""
    axarr = ""
    changingIndex = 0

    def plot(self, filename):
        fig = plt.figure()
        self.ax = fig.add_subplot(121, projection='3d')
        self.data = dataSuite.readDataFile(filename)
        self.changingIndex = randint(0,len(self.data) -1)
        errorSurface = plotErrorSurface(5, self.data)

        self.ax.plot_surface(errorSurface[0], errorSurface[1],errorSurface[2])

        self.axarr = fig.add_subplot(122)
        for i in range(0,len(self.data)):
            if self.data[i][0] == 1:
                self.axarr.scatter(self.data[i][1],self.data[i][2],20, 'r')
            else:
                self.axarr.scatter(self.data[i][1],self.data[i][2],20, 'y')
        ani1 = animation.FuncAnimation(fig,self.animateError, interval=1000)

        self.ax.set_xlabel('W1 Axis')
        self.ax.set_ylabel('W2 Axis')
        self.ax.set_zlabel('Error Axis; iteration:%d'%self.iterations,)

        plt.show()

    def animateError(self,i):
        self.iterations +=1
        self.data[self.changingIndex][1] += self.deltaX
        self.data[self.changingIndex][2] += self.deltaY
        if self.data[self.changingIndex][1] < -10:
            self.deltaX *= -1
        if self.data[self.changingIndex][1] > 10:
            self.deltaX *= -1
        if self.data[self.changingIndex][2] < -10:
            self.deltaY *= -1
        if self.data[self.changingIndex][2] > 10:
            self.deltaY *= -1
        self.ax.clear()
        errorSurface = plotErrorSurface(5, self.data)
        self.ax.plot_surface(errorSurface[0], errorSurface[1],errorSurface[2],rstride=1, cstride=1, cmap=cm.coolwarm)
        self.ax.set_xlabel('W1 Axis')
        self.ax.set_ylabel('W2 Axis')
        self.ax.set_zlabel('Error Axis; iteration:%d'%i,)
        self.axarr.clear()
        for i in range(0,len(self.data)):
            if self.data[i][0] == 1:
                self.axarr.scatter(self.data[i][1],self.data[i][2],20, 'r')
            else:
                self.axarr.scatter(self.data[i][1],self.data[i][2],20, 'y')
