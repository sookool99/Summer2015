# Data File generator

## importing Data Suites
It is as simple as adding this line to your imports 
```
from data import dataSuit
```

## Read In a Data file
NOTE: format of the data file has to be in a specific csv format following format that is each line should be as follow:
`expectedValue,x1,x2` where expected value is an int, and the other two are floats.

This file will read in a file and format the proper variables and pass back lists. data file can be any name, however must be in the dataFile folder

### Examples
For default params you must have a `Data.txt` file in dataFiles folder
```
data.readDataFile()
```

To Specify what data file you want to read
```
data.readDataFile('MyDataFile.txt')
```


## Polynomialy seperated data:
generates a data set that is seperated by up to a 5th degree polynomial

### Examples

```
x = generatePolynomialData([0,0,0,1,1], [[-5,5],[0,5]])
```
or to save file to not standard Data.txt filename
```
x = generatePolynomialData([1,1,2,1,1], [[-5,5],[0,5]], 500,True, 'test3.txt')
```

## Gaussian Clusters

### Examples

#### Create as many clusters as you want
```
mean1 = [0,0]
cov1 = [[10,0],[0,10]]
cluster1 = [mean1,cov1, 1]

mean2 = [30,30]
cov2 = [[10,0],[0,10]]
cluster2 = [mean2,cov2, 0]
clusters = [cluster1, cluster2]
```

### Then to run
```
x = generate2DGausData(clusters)
```
or to save file to not standard Data.txt filename
```
x = generate2DGausData(clusters, 100,False, 'test.txt')
```