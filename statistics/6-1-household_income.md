[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

>> In this exercise, I compute several statistics to look at income distribution.

>> With upper bound set at $1,000,000:
```
Mean Income: 74278.7075312
Median Income: 51226.9330656
Standard Deviation: 93946.9299635
Skeness: 4.94992024443
Pearson's skewness: 0.736110519243
Percent of respondants below mean income: 66.000587956687198
```

>> And with upper bound set at $10,000,000:
```
Mean Income: 124267.397222
Median Income: 51226.9330656
Standard Deviation: 559608.501374
Skeness: 11.6036902675
Pearson's skewness: 0.391561943627
Percent of respondants below mean income: 85.656306652076637
```

>> So it looks like that increasing the upper bound of the reported income, skewness increases, but Pearson's decreases

>> Python code Below:

```python
import thinkstats2
import thinkplot
import hinc
import hinc2
import numpy as np
import math

## Skewness and related functions borrowed from Think Stats book
def RawMoment(xs, k):
    return sum(x**k for x in xs) / len(xs)
def CentralMoment(xs, k):
    mean = RawMoment(xs, 1)
    return sum((x - mean)**k for x in xs) / len(xs)
def StandardizedMoment(xs, k):
    var = CentralMoment(xs, 2)
    std = math.sqrt(var)
    return CentralMoment(xs, k) / std**k
def Skewness(xs):
    return StandardizedMoment(xs, 3)

def main():
    ## Read income data from hinc.py provided in Think Stats
    data = hinc.ReadData()

    ## Get an interpolated sample to model the income data in log scale. Default upper bound is 10^6
    log_sample = hinc2.InterpolateSample(data)

    ## Plot the CDF
    log_cdf = thinkstats2.Cdf(log_sample)
    thinkplot.Cdf(log_cdf)
    #thinkplot.Show(xlabel='Income', ylabel='CDF')

    ## Calculate statistics
    sample = np.power(10, log_sample)

    mean = np.mean(sample)
    median = np.median(sample)
    std = np.std(sample)
    skewness = Skewness(sample)
    pearson = 3*(mean-median)/std

    print 'Mean Income:', mean
    print 'Median Income:', median
    print 'Standard Deviation:', std
    print 'Skeness:', skewness
    print "Pearson's skewness:", pearson

    cdf = thinkstats2.Cdf(sample)
    print 'Percent of respondants below mean income: %r' %(cdf[mean]*100)

if __name__ == '__main__':
    main()
```
