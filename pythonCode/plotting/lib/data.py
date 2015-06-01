__author__ = 'shawn'
import csv
import matplotlib.pyplot as plt

def plotData(w1,w2,data):
    if(isinstance(data,str) or not len(data)):
        if not len(data):
            data = "dataFiles/Data.txt"
        dataFile = []
        with open(data) as fp:
            reader = csv.reader(fp, delimiter=',')
            for line in reader:
                dataFile.append([int(line[0]), float(line[1]), float(line[2])])
        data = dataFile
    for i in range(0,len(data)):
        if data[i][0] == 1:
            plt.scatter(data[i][1],data[i][2],20, 'r')
        else:
            plt.scatter(data[i][1],data[i][2],20, 'y')
    plt.plot([0,w1],[0,w2])
    plt.show()