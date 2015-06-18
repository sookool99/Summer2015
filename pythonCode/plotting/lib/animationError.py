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
def generate_graph_data(numberOfEach):
    x = np.linspace(-10, 10, numberOfEach)
    y = np.linspace(-10, 10, numberOfEach)
    x, y = np.meshgrid(x, y)
    return [x, y]


# used to generate a gride and then calculate the error
def plot_error_surface(number_of_each=20, data=[]):
    data_points = generate_graph_data(number_of_each)
    x_holder = data_points[0]
    y_holder = data_points[1]
    z = np.array([calculate.calculate_error(x, y, data, False) for x, y in zip(np.ravel(x_holder), np.ravel(y_holder))])
    Z = z.reshape(x_holder.shape)
    data_points.extend([Z])
    return data_points


class AnimatedPlot:

    def __init__(self):
        self.iterations = 0
        self.deltaX = 1
        self.deltaY = -2
        self.data = []
        self.ax = ""
        self.axarr = ""
        self.changingIndex = 0

    def plot(self, filename):
        fig = plt.figure()
        self.ax = fig.add_subplot(121, projection='3d')
        self.data = dataSuite.read_data_file(filename)
        self.changingIndex = randint(0, len(self.data) - 1)
        error_surface = plot_error_surface(5, self.data)

        self.ax.plot_surface(error_surface[0], error_surface[1], error_surface[2])

        self.axarr = fig.add_subplot(122)
        for i in range(0, len(self.data)):
            if self.data[i][0] == 1:
                self.axarr.scatter(self.data[i][1], self.data[i][2], 20, 'r')
            else:
                self.axarr.scatter(self.data[i][1], self.data[i][2], 20, 'y')
        ani1 = animation.FuncAnimation(fig, self.animate_error, interval=1000)

        self.ax.set_xlabel('W1 Axis')
        self.ax.set_ylabel('W2 Axis')
        self.ax.set_zlabel('Error Axis; iteration:%d' % self.iterations, )

        plt.show()

    def animate_error(self, i):
        self.iterations += 1
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
        error_surface = plot_error_surface(5, self.data)
        self.ax.plot_surface(error_surface[0], error_surface[1], error_surface[2], rstride=1, cstride=1, cmap=cm.coolwarm)
        self.ax.set_xlabel('W1 Axis')
        self.ax.set_ylabel('W2 Axis')
        self.ax.set_zlabel('Error Axis; iteration:%d' % i, )
        self.axarr.clear()
        for i in range(0, len(self.data)):
            if self.data[i][0] == 1:
                self.axarr.scatter(self.data[i][1], self.data[i][2], 20, 'r')
            else:
                self.axarr.scatter(self.data[i][1], self.data[i][2], 20, 'y')
