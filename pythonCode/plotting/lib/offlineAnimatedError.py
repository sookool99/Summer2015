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
class AnimatedPlot:

    def __init__(self):
        self.iteration = 0
        self.delta_X = 1
        self.delta_Y = -2
        self.data = []
        self.error_data = []
        self.ax = ""
        self.axarr = ""
        self.change_index = 0
        self.mesh_number = 0
        self.ani1 = None
        self.mesh_x = None
        self.mesh_y = None

    def plot(self,data_file_name, offline_data_file_name):
        fig = plt.figure(figsize=(20,10))
        self.ax = fig.add_subplot(121, projection='3d')
        self.error_data = []

        with open('dataFiles/' + offline_data_file_name) as fp:
            reader = csv.reader(fp, delimiter=',')
            for line in reader:
                if len(line) == 5:
                    self.delta_X, self.delta_Y, self.change_index, self.iteration, self.mesh_number = [float(x) for x in line]
                else:
                    self.error_data.append([float(x) for x in line])
        self.iteration = int(self.iteration)
        self.change_index = int(self.change_index)
        self.axarr = fig.add_subplot(122)
        self.data = []
        with open('dataFiles/'+ data_file_name) as fp:
            reader = csv.reader(fp, delimiter=',')
            for line in reader:
                self.data.append([int(line[0]), float(line[1]), float(line[2])])
        for i in range(0,len(self.data)):
            if self.data[i][0] == 1:
                self.axarr.scatter(self.data[i][1],self.data[i][2],20, 'r')
            else:
                self.axarr.scatter(self.data[i][1],self.data[i][2],20, 'y')

        self.mesh_x = np.linspace(-10,10,self.mesh_number)
        self.mesh_y = np.linspace(-10,10,self.mesh_number)
        self.mesh_x, self.mesh_y = np.meshgrid(self.mesh_x,self.mesh_y)
        self.ani1 = animation.FuncAnimation(fig,self.animate_error, interval=1000)

        self.ax.set_xlabel('W1 Axis')
        self.ax.set_ylabel('W2 Axis')
        self.ax.set_zlabel('Error Axis')

        plt.show()

    def animate_error(self,i):
        self.axarr.clear()
        for x in range(0,len(self.data)):
            if self.data[x][0] == 1:
                self.axarr.scatter(self.data[x][1],self.data[x][2],20, 'r')
            else:
                self.axarr.scatter(self.data[x][1],self.data[x][2],20, 'y')
        self.data[self.change_index][1] += self.delta_X
        self.data[self.change_index][2] += self.delta_Y
        if self.data[self.change_index][1] < -10:
            self.delta_X *= -1
        if self.data[self.change_index][1] > 10:
            self.delta_X *= -1
        if self.data[self.change_index][2] < -10:
            self.delta_Y *= -1
        if self.data[self.change_index][2] > 10:
            self.delta_Y *= -1
        self.ax.clear()
        errorSurface = np.asarray(self.error_data[i % self.iteration ]).reshape(self.mesh_x.shape)
        self.ax.plot_surface(self.mesh_x, self.mesh_y,errorSurface,rstride=1, cstride=1, cmap=cm.coolwarm)
        self.ax.set_xlabel('W1 Axis')
        self.ax.set_ylabel('W2 Axis')
        self.ax.set_zlabel('Error Axis; iteration:%d'%i,)