# Solving the Minimum and Maximum Sums Within a List with One Removed Element

The following is a solution to https://www.hackerrank.com/challenges/mini-max-sum/problem, in which a Python script must return the minimum and maximum possible values that can be created by summing the values of a list after removing any one element. A full summary of the problem (and an example answer) can be found below

# The Problem
![alt text](https://github.com/Fehiroh/hackerrank_problem_solving_MinMaxSum/blob/master/mini-max-sum-English.jpg "Logo Title Text 1")

# The Solution 
## Importing Libraries

``` python 
import math
import os
import random
import re
import sys
```
## Defining the Function
While the minimum and maximum possible sums of `arr` are what we are ultimately after, running through each possible sum is unneccessary. Instead, it's much more efficient to calculate the initial sum (`init_sum`), find the maximum and minimum values (`min_val` and `max_val`) within the list, and substract each from the initial sum.

In order to do this, we need an initial comparitor for, which we obtain by assigning the value of the first element to two variables, `min_val` and `max_val`. Next, we cycle through each element of `arr` via index, overwriting `min_val` and `max_val` as appropriate. Finally, we print the answer. 

```python
#   Solution 
def miniMaxSum(arr):
    init_sum = sum(arr)
    min_val = arr[0]
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
        elif arr[i] > max_val:
            max_val = arr[i]
    print(init_sum-max_val, init_sum-min_val)


# Execution
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
```

## Explanation: Why Not Sort?

Maybe you're wondering why we didn't just use a sorting method and then index to find the minimum and maximum values. After all, that's much less code, and should also return what we are after, right? 

The primary reason is that sorts don't scale well. As you increase the length of `arr` that method would get slower and slower. This can be a worthwhile trade-off if you do infact need the entire sorted list. However, since we would immediately discard everything except the min and max, it makes more sense to only ever compare against these values. 


## Alternate Code

Here's an alternate version: 

```python
#   Solution 
def miniMaxSum(arr):
    init_sum = sum(arr)
    min_val = min(arr)
    max_val = max(arr)
    print(init_sum-max_val, init_sum-min_val)
```


