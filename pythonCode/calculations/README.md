# Calculation files

All functions

* calulating error
* calculating offline animated error data
* finding weights

## importing the files
It is as simple as adding this line to your imports 
```
from calculations import calculation as calc
```

## Calculate The Error
Given Two weight vectors this function will calculate the error for those specific weights on a dataFile, which you can pass
the actual data, or data file name, or just use default  which is `Data.txt`

### Examples
```
err = calc.calculateError(1,1)
```

You can optionally pass either data, or a dataFileName for this function to read it.
```
err = calc.calculateError(1,1,myData)
err = calc.calculateError(1,1,'fileName')
```

if you wish not to display the output from the calculation just pass a last param with false
```
err = calc.calculateError(1,1,myData, false)
```

## Calculate The Offline Error Data
Will calculate the data required for doing offline calculation to have for doing animated error surface.

### Examples
using all defauts requires
```
calc.calcOfflineData()
```

or using any of the params you can pass
```
calc.calcOfflineData(deltaX = 1, deltaY = -2, data = [], meshNumber = 10,iterations = 10, fileName = "offlineErrorData.txt")
```

## find weights
will attempt to find weights for a given dataset.

### Examples
using `Data.txt` file with default params
```
calc.findWeights()
```

however you can pass either a data file or a name of a data file
```
calc.findWeights(myData)
calc.findWeights('fileName.txt')
```

or any number of the other params
```
calc.findWeights(data = [],plot = True, showError = True, epsilon = 0.1)
```






