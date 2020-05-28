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



## Alternate Code

The following are alternate snippets of code that solve the problem in similar ways, but which are much less efficient, I've included them below as a fun teachable moment. They are arranged from the least efficient at the top, to the most efficient at the bottom. 


### Calculating Every Possible Sum 

An easy mistake to make in coding, especially when you're new, is to take the problem statement at face-value. If we want the highest and lowest sums, I should calulate the sum of each possible solution, and keep the ones which meet the criteria. Something like this: 

```python
#  Alt Solution: Sort
def miniMaxSum(arr):
    init_sum_ar = del 
    min_sum = init_sum - max_val
    max_sum = init_sum - min_val
    print(min_sum, max_sum)
```


 While understandable, this is a *terrible* way to go abo



### Using a Sort

Maybe you're wondering why we didn't just use a sorting method and then index to find the minimum and maximum values. After all, that's much less code, and should also return what we are after, right? Something like this:

```python
#  Alt Solution: Sort
def miniMaxSum(arr):
    sort_ar = ar.sort()
    min_val = sort_ar[0]
    max_val = sort_ar[len(sort_ar)]
    min_sum = init_sum - max_val
    max_sum = init_sum - min_val
    print(min_sum, max_sum)
```

The primary reason is that sorts don't scale well, since each element needs to be compare against multiple elements. As you increase the length of `arr` that method would get slower and slower. This can be a worthwhile trade-off if you do infact need the entire sorted list. However, since we would immediately discard everything except the min and max, it makes more sense to only ever compare against these values. 



```python
#   Solution 
def miniMaxSum(arr):
    init_sum = sum(arr)
    min_val = min(arr)
    max_val = max(arr)
    min_sum = init_sum - max_val
    max_sum = init_sum - min_val
    print(min_sum, max_sum)
```

It is much easier to read, but is disadvantaged in that making use of `min()` and `max()` requires two iterations through `arr` thereby making the function twice as slow. Personally, I prefer the first since it is extremely scalable.


