[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

>> In this exercise, I use a resampling process to test the difference between pregnancy length and
>> birth weight for firstborns vs. others. The test show a p value of 0.17 which is too high to reject the null hypothesis.
>> But the result is about the same as a permutation process.  
>> Python code is below:

```python
import hypothesis
import first
import numpy as np

## Define new class and inheritng from DiffMeansPermute from hypothesis file
class DiffMeansResample(hypothesis.DiffMeansPermute):
    ## Overriding RunModel to do resampling
    def RunModel(self):
        group1 = np.random.choice(self.pool, self.n, replace=True)
        group2 = np.random.choice(self.pool, self.m, replace=True)
        return group1, group2

def main():
    live, firstborn, others = first.MakeFrames()
    ## Run resampling tests

    data = firstborn.prglngth.values, others.prglngth.values
    resampled = DiffMeansResample(data)
    p = resampled.PValue(iters=10000)

    print 'Means permute preglength'
    print 'p-value = %r' %p
    print 'actual = %r' %resampled.actual
    print 'ts max = %r' %resampled.MaxTestStat()

if __name__ == "__main__":
    main()
```
