__author__ = 'shawn'
from plotting.lib import data
from plotting.lib import animationError
from plotting.lib import offlineAnimatedError


def plot_data(w1=0, w2=0, data_file=[]):
    data.plot_data(w1, w2, data_file)


def animated_error(filename="Data.txt"):
    a = animationError.AnimatedPlot()
    return a.plot(filename)


def offline_error_animated(filename="Data.txt", offline_data_file_name='offlineErrorData.txt'):
    a = offlineAnimatedError.AnimatedPlot()
    return a.plot(filename, offline_data_file_name)
