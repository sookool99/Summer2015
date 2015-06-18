__author__ = 'shawn'
import numpy as np
import matplotlib.pyplot as plt
import theano
import csv

folderName = 'dataFiles/'

def generate_2d_gauss_data(dataPoints, size, display, ofName):
    points = []
    if ofName:
        data = open(folderName + ofName, "w")
        writer = csv.writer(data, delimiter=',')
    for i in range(0, len(dataPoints)):
        x, y = np.random.multivariate_normal(dataPoints[i][0], dataPoints[i][1], size).T
        for kk in range(0, size):
            points.extend([[dataPoints[i][2], x[kk], y[kk]]])
            if ofName:
                writer.writerow([dataPoints[i][2], x[kk], y[kk]])
        if display:
            if dataPoints[i][2]:
                plt.scatter(x, y, 20, 'r')
            else:
                plt.scatter(x, y, 20, 'y')
    if ofName:
        data.close()
    if display:
        plt.show()
    return points
