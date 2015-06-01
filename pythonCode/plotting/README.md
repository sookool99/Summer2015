# Data File generator

## importing the plot
It is as simple as adding this line to your imports 
```
from plotting import plot
```

## Plot The Data
Plots out the data on a 2d plot.

### examples
* To Plot data from "Data.txt" <br>
```
plot.plotData()
```

* You can also pass it two optional weights <br>
```
plot.plotData(1,1)
```

* and you can also pass it optionally a data file (already loaded) or a string which is the name of another data file you want to read <br>
```
plot.plotData(0,0,myData)
plot.plotData(0,0,'myFile.txt')
```

## Plot Animated Error
NOTE: this does the calculations as it runs so it may be slow! suggest using offline error plotting.

This function will plot the data error surface as a single (random) point changes.

### Examples
* called with default params means you have a `Data.txt` file. <br>
```
plot.animatedError()
```

* You can optionally pass your own data fileName as a string <br>
```
plot.animatedError('myFileName')
```

## Plot offline Animated Error
NOTE: For this to work you must run the offline data calculation file which can be found in `calculations.calculateOfflineAnimationError`

This function will plot the data error surface as a single (random) point changes for an offline file which make it run smoother.

### Examples
* called with default params means you have a `Data.txt` file and `offlineErrorData.txt` file.<br>
```
plot.offlineErrorAnimated()
```

* You can optionally pass your own data fileName as a string or an offLine data fileName<br>
```
plot.offlineErrorAnimated('mydataFileName')
plot.offlineErrorAnimated('mydataFileName', 'myOfflineDataFile')
```
