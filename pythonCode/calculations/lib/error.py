__author__ = 'shawn'
import theano
import theano.tensor as T
import csv


def calculate(w1, w2, data, display):
    x = T.vector('x')
    w = T.vector('w')

    s = 1 / (1 + T.exp(-T.dot(x, w)))
    logistic = theano.function([x, w], s)

    if display:
        print("With: w1 = %f and w2 = %f" % (w1, w2))

    sum_error = 0
    sum_error_square = 0
    if isinstance(data, str) or not len(data):
        if not len(data):
            data = 'Data.txt'
        with open('dataFiles/' + data) as fp:
            reader = csv.reader(fp, delimiter=',')
            for line in reader:
                data.append([int(line[0]), float(line[1]), float(line[2])])
    if display:
        print('y\t\tf(x)\t\tE\t\tE^2')
    for i in range(0, len(data)):
        x1 = data[i][1]
        x2 = data[i][2]
        f = logistic([x1, x2], [w1, w2])
        e = data[i][0] - f
        e2 = e ** 2
        sum_error += e
        sum_error_square += e2
        if display:
            print('%f\t%f\t%f\t%f' % (data[i][0], f, e, e2))
    if display:
        print("\nSum:\t\t\t\t%f\t%f" % (sum_error, sum_error_square))
    return sum_error_square
