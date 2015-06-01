__author__ = 'shawn'

import numpy as np
import matplotlib.pyplot as plt
import theano
import theano.tensor as T
import csv
from data.lib import polyData
from data.lib import gaussData

def generatePolynomial(coef, dataRange, size = 500, display = True, ofName = ''):
    polyData.generatePolynomialData(coef, dataRange, size, display, ofName)

def generateGauss(dataPoints, size = 500, display = True, ofName = ''):
    gaussData.generate2DGaussData(dataPoints, size, display, ofName)

def readDataFile(filename = 'Data.txt'):
    dataFile = []
    with open('dataFiles/' + filename) as fp:
        reader = csv.reader(fp, delimiter=',')
        for line in reader:
            dataFile.append([int(line[0]), float(line[1]), float(line[2])])
    return dataFile