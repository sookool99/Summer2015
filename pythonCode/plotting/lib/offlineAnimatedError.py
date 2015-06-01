__author__ = 'shawn'
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
# import is not used but it is needed.
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import csv

# offLine animated error plot surface
# you must have run calcOfflineData(0.25,-0.5,40, 40) with what I suggest those parameters, it will take a long time
# to run but it will give the best results.
class animatedPlot:

    iterations = 0
    deltaX = 1
    deltaY = -2
    data = []
    errorData = []
    ax = ""
    axarr = ""
    changingIndex = 0

    def plot(self,dataFileName, offlineDataFileName):
        fig = plt.figure(figsize=(20,10))
        self.ax = fig.add_subplot(121, projection='3d')
        self.errorData = []

        with open('dataFiles/' + offlineDataFileName) as fp:
            reader = csv.reader(fp, delimiter=',')
            for line in reader:
                if len(line) == 5:
                    self.deltaX, self.deltaY, self.changeIndex, self.iteration, self.meshNumber = [float(x) for x in line]
                else:
                    self.errorData.append([float(x) for x in line])
        self.iteration = int(self.iteration)
        self.changeIndex = int(self.changeIndex)
        self.axarr = fig.add_subplot(122)
        self.data = []
        with open('dataFiles/'+ dataFileName) as fp:
            reader = csv.reader(fp, delimiter=',')
            for line in reader:
                self.data.append([int(line[0]), float(line[1]), float(line[2])])
        for i in range(0,len(self.data)):
            if self.data[i][0] == 1:
                self.axarr.scatter(self.data[i][1],self.data[i][2],20, 'r')
            else:
                self.axarr.scatter(self.data[i][1],self.data[i][2],20, 'y')

        self.meshx = np.linspace(-10,10,self.meshNumber)
        self.meshy = np.linspace(-10,10,self.meshNumber)
        self.meshx, self.meshy = np.meshgrid(self.meshx,self.meshy)
        self.ani1 = animation.FuncAnimation(fig,self.animateError, interval=1000)

        self.ax.set_xlabel('W1 Axis')
        self.ax.set_ylabel('W2 Axis')
        self.ax.set_zlabel('Error Axis')

        plt.show()

    def animateError(self,i):
        self.axarr.clear()
        for x in range(0,len(self.data)):
            if self.data[x][0] == 1:
                self.axarr.scatter(self.data[x][1],self.data[x][2],20, 'r')
            else:
                self.axarr.scatter(self.data[x][1],self.data[x][2],20, 'y')
        self.data[self.changeIndex][1] += self.deltaX
        self.data[self.changeIndex][2] += self.deltaY
        if self.data[self.changeIndex][1] < -10:
            self.deltaX *= -1
        if self.data[self.changeIndex][1] > 10:
            self.deltaX *= -1
        if self.data[self.changeIndex][2] < -10:
            self.deltaY *= -1
        if self.data[self.changeIndex][2] > 10:
            self.deltaY *= -1
        self.ax.clear()
        errorSurface = np.asarray(self.errorData[i % self.iteration ]).reshape(self.meshx.shape)
        self.ax.plot_surface(self.meshx, self.meshy,errorSurface,rstride=1, cstride=1, cmap=cm.coolwarm)
        self.ax.set_xlabel('W1 Axis')
        self.ax.set_ylabel('W2 Axis')
        self.ax.set_zlabel('Error Axis; iteration:%d'%i,)