__author__ = 'shawn'
import numpy as np
import csv
from random import randint
import sys
from calculations.lib import error


def calc_offline_data(delta_x, delta_y, data, mesh_number, iterations, file_name):
    data = []
    x = np.linspace(-10, 10, mesh_number)
    y = np.linspace(-10, 10, mesh_number)
    x, y = np.meshgrid(x, y)
    if isinstance(data, str) or not len(data):
        if not len(data):
            data = 'Data.txt'
        with open('dataFiles/' + data) as fp:
            reader = csv.reader(fp, delimiter=',')
            for line in reader:
                data.append([int(line[0]), float(line[1]), float(line[2])])

    changing_index = randint(0, len(data) - 1)

    data_file = open(file_name, "w")
    writer = csv.writer(data_file, delimiter=',')
    writer.writerow([delta_x, delta_y, changing_index, iterations, mesh_number])

    for i in range(0, iterations):
        print("On Iteration %d of moving points" % i)
        sys.stdout.flush()
        data[changing_index][1] += delta_x
        data[changing_index][2] += delta_y
        if data[changing_index][1] < -10:
            delta_x *= -1
        if data[changing_index][1] > 10:
            delta_x *= -1
        if data[changing_index][2] < -10:
            delta_y *= -1
        if data[changing_index][2] > 10:
            delta_y *= -1
        counter = 0
        total_iter = mesh_number ** 2
        print("Done(out of %d):" % total_iter, end="")
        z_data = []
        for X, Y in zip(np.ravel(x), np.ravel(y)):
            z_data.extend([error.calculateError(X, Y, data, False)])
            if counter % int((total_iter / 10)) == 0:
                print(" %d" % counter, end="")
            counter += 1
        z = np.array(z_data)
        print('\n', end="")
        writer.writerow(z)
    data_file.close()
    print("Done Offline Calculations!")
