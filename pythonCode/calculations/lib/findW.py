__author__ = 'shawn'
import numpy as np
import theano
import theano.tensor as T
import csv
from calculations.lib import error

def find(data, plot, showError, epsilon):
    x = T.vector('x')
    w = T.vector('w')

    s = 1 / (1 + T.exp(-T.dot(x,w)))
    logistic = theano.function([x,w], s)

    gs = T.grad(s, w)
    dlogistic = theano.function([x,w], gs)

    w1 = np.random.uniform(-2,2,1)[0]
    w2 = np.random.uniform(-2,2,1)[0]
    print("Starting Values: w1 = %f and w2 = %f"%(w1,w2))

    if(isinstance(data,str) or not len(data)):
        if not len(data):
            data = 'Data.txt'
        with open('dataFiles/' + data) as fp:
            reader = csv.reader(fp, delimiter=',')
            for line in reader:
                data.append([int(line[0]), float(line[1]), float(line[2])])
    sumErrorSquare = 1
    iterations = 0
    while sumErrorSquare > epsilon:
        sumError = 0
        sumErrorSquare = 0
        sumErrorDeriv = 0
        for i in range(0,len(data)):
            x1 = data[i][1]
            x2 = data[i][2]
            f = logistic([x1,x2],[w1,w2])
            e = data[i][0] - f
            e2 = e**2
            sumError += e
            sumErrorSquare = sumErrorSquare + e2
            sumErrorDeriv -= 2 * e * dlogistic([x1,x2],[w1,w2])
        if iterations > 200:
            print("either The Data given is unsolvable or you have reached a local minima ... ")
            return error.calculateError(w1,w2, showError)
        iterations += 1
        w1 = w1 -  0.1 * sumErrorDeriv[0]
        w2 = w2 - 0.1 * sumErrorDeriv[1]
    print("Final Values: w1 = %f and w2 = %f"%(w1,w2))
    print("iterations took:",iterations)
    if plot:
        plot.plotData(w1,w2,data )
    if showError:
        print("\nCalculating Error ... ")
    return error.calculateError(w1,w2, showError)
