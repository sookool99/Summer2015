__author__ = 'shawn'
from calculations.lib import error
from calculations.lib import offlineData
from calculations.lib import findW


def calculate_error(w1, w2, data=[], display=True):
    return error.calculate(w1, w2, data, display)


# you must have a file called Data.txt where it will be your training data will be saved to. suggest using my data
# generation files in my format.
def calculate_offline_animation_error(delta_x=1, delta_y=-2, data=[], mesh_number=10, iterations=10,
                                      file_name="offlineErrorData.txt"):
    return offlineData.calc_offline_data(delta_x, delta_y, mesh_number, iterations, file_name)


# Only works with 2 inputs to find 2 weights
def find_weights(data=[], plot=True, show_error=True, epsilon=0.1):
    return findW.find(data, plot, show_error, epsilon)
