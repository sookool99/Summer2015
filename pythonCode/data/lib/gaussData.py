__author__ = 'shawn'
import numpy as np
import matplotlib.pyplot as plt
import theano
import csv
folderName = 'dataFiles/'
#generates len(dataPoints) amount of gause clusters
#@dataPoints: is a list of mean and covariance's to generate data for.
#       Which look something like [[mean1, cov1, value1], [mean2,cov2,value2]] where mean is a 1X2 and cov is 2X2
#       and value is what the value for this cluster will be, which is a truthy value.
#@size: size of data points you want per cluster
#@display: true of false if you want to display data on plot or not
#@ofName: out file name where to save data to. If you do not wish to save the data to a file
#       Then just dont pass anything for this param.
def generate2DGaussData(dataPoints, size, display, ofName):
    points = []
    if ofName:
        data = open(folderName + ofName, "w")
        writer = csv.writer(data, delimiter=',')
    for i in range(0,len(dataPoints)):
        x,y = np.random.multivariate_normal(dataPoints[i][0], dataPoints[i][1], size).T
        for kk in range(0,size):
            points.extend([[dataPoints[i][2],x[kk],y[kk]]])
            if ofName:
                writer.writerow([dataPoints[i][2],x[kk],y[kk]])
        if display:
            if dataPoints[i][2]:
                plt.scatter(x,y,20, 'r')
            else:
                plt.scatter(x,y,20, 'y')
    if ofName:
        data.close()
    if display:
        plt.show()
    return points