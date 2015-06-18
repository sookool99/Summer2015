__author__ = 'shawn'

import numpy as np
import matplotlib.pyplot as plt
import theano
import theano.tensor as T
import csv
from data.lib import polyData
from data.lib import gaussData


def generate_polynomial(coef, data_range, size=500, display=True, of_name=''):
    polyData.generate_polynomial_data(coef, data_range, size, display, of_name)


def generate_gauss(data_points, size=500, display=True, of_name=''):
    gaussData.generate_2d_gauss_data(data_points, size, display, of_name)


def read_data_file(filename='Data.txt'):
    data_file = []
    with open('dataFiles/' + filename) as fp:
        reader = csv.reader(fp, delimiter=',')
        for line in reader:
            data_file.append([int(line[0]), float(line[1]), float(line[2])])
    return data_file
