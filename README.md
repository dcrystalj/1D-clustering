# 1D array Groups finder

Groups finder for 1 dimensional array using hirarhical clustering with parameters to get number of groups you want. This algorithm foces group to be in closest distance. 


## correct example
``` in = 1 1 1 5 6 6 6 1 1 6 ```

``` out = 1 1 1 1 1 1 1 1 0 0 0 ```

## wrong example
``` in = 1 1 1 5 6 6 6 1 1 6 ```
There is no way to have example like this ``` out = 0 0 0 1 1 1 1 0 0 1``` because group with 1 is saperated with group of 0.


At the beginning it use moving average filter because i needed it

Similar projet to this is:
https://github.com/MKolman/list-partiotioner
