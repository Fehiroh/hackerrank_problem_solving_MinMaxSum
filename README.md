# Solving the Minimum and Maximum Sums Within a List with One Removed Element

The following is a solution to https://www.hackerrank.com/challenges/mini-max-sum/problem, in which a Python script must return the minimum and maximum possible values that can be created by summing the values of a list after removing any one element. This must also be done as quickly as possible, which means that the solution must account for scaling.  A full summary of the problem (and an example answer) can be found below.

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
    min_sum = init_sum - max_val
    max_sum = init_sum - min_val 
    print(min_sum, max_sum)


# Execution
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
```



## Alternate Code

In order to explain *why* this code is a great solution,  I've written some alternate snippets of code that solve the problem in several less efficient ways. I've included them below, and will go through how their logic works, and how they compare to the original solution. They are arranged according to effiency, with the least efficient at the top and the most efficient at the bottom. 


### Calculating Every Possible Sum 

An easy mistake to make in coding, especially when you're new, is to take the problem statement at face-value. If we want the highest and lowest sums possible  after removing one element, I should calulate the sum of each possible solution, and keep the ones which meet the criteria. I should create initial `min_sum`s and `max_sum` by summing without any one given element, create every possible sum, and running comparisons to find the real `min_sum` and `max_sum`.  The code would look something like this: 

```python
#  Alt Solution: Every possible sum
def miniMaxSum(arr):

    # initial values
    pop = arr.pop()
    max_sum, min_sum = sum(arr)
    arr = arr.append(pop)
    
    # comparisons 
    for i in range(1, len(arr)): 
        new_arr = arr.copy()
        del new_arr[i]
        new_sum = sum(new_arr)
            if new_sum < min_sum:
                min_sum = new_sum
            elif new_sum > max_sum:
                max_sum = new_sum
    print(min_sum, max_sum)
```


 While understandable, this is a *terrible* way to go about solving this problem. Firstly, the code is longer and harder to read than the "optimal" solution, but it also requires every element to be run through a `sum()` function `len(arr)` times, and the entire array to be duplicated `len(arr)` times. When you are dealing with data structures that contain observations in the millions or billions, this function would take hours to run. It is particularily worth noting that  none of the other solutions require an `x.copy()`, while this solution does. This means that a significant portion of run-time is 100% unnecessary outside of having failed to reframe the problem. This solution is unlikely to be written by hand, since the implementation requires enough coding accumen / language knowledge that one would probably 


### Using a Sort

Maybe you're wondering why we didn't just use a sorting method and then index to find the minimum and maximum values. After all, that's much less code, and should also return what we are after, right? Something like this:

```python
#  Alt Solution: Sort
def miniMaxSum(arr):
    init_sum = sum(arr)
    sort_ar = arr.sort()
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

It is much easier to read, but is disadvantaged in that making use of `min()` and `max()` requires two iterations through `arr` thereby making the function twice as slow. This is nice in that it's still scaling linearly, which makes it much more efficient than previous iteractions, buthalf the speed is still not great. 


