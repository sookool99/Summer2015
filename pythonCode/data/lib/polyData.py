__author__ = 'shawn'
import numpy as np
import matplotlib.pyplot as plt
import theano
import csv

folderName = 'dataFiles/'

# @coef: list a coefficients of degree 5 polynomial, where [a,b,c,d,e] belongs to ax^5 + bx^4 + cx^3 +dx^2 + e
# @dataRange: list of [xRange, yRange]. for example [[-5,5],[0,5]]
# @size: number of data points you want
# @display: true of false if you wish to see what data looks like on plot
# @ofName: out file name where to save data to. If you do not wish to save the data to a file
#       Then just dont pass anything for this param.
def generate_polynomial_data(coef, dataRange, size, display, ofName):
    x = np.random.uniform(dataRange[0][0],dataRange[0][1],size)
    y = np.random.uniform(dataRange[1][0],dataRange[1][1],size)

    if ofName:
        data = open(folderName + ofName, "w")
        writer = csv.writer(data, delimiter=',')
    points = []
    for i in range(0,size):
        fx = calculate_polynomial(x[i], coef)
        if y[i] > fx:
            points.extend([[1,x[i],y[i]]])
            if ofName:
                writer.writerow([1,x[i],y[i]])
            if display:
                plt.scatter(x[i],y[i],20,'r')
        else:
            points.extend([[0,x[i],y[i]]])
            if ofName:
                writer.writerow([0, x[i], y[i]])
            if display:
                plt.scatter(x[i], y[i], 20, 'y')
    if ofName:
        data.close()
    if display:
        x1 = np.linspace(dataRange[0][0],dataRange[0][1],size)
        plt.plot(x1, coef[0]*x1**5 + coef[1]*x1**4 + coef[2]*x1**3 + coef[3]*x1**2 + coef[4])
        plt.axis([dataRange[0][0] - 2, dataRange[0][1] + 2, dataRange[1][0] - 2, dataRange[1][1] + 2])
        plt.show()
    return points

# function only used for generatePolynomialData() no need to test this function ...
def calculate_polynomial(x, coef):
    return coef[0]*x**5 + coef[1]*x**4 + coef[2]*x**3 + coef[3]*x**2 + coef[4]