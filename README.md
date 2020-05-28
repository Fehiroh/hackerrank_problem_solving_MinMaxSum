# A Case-study in Optimization: Designing a Function to Return the Minimum and Maximum Sums of a List with One Removed Element

# Introduction 
Squeezing a little more speed out of your code can be extremely important, especially when dealing with Big Data, which is becoming increasing prevalent in the Tech sector. In order to go about making better code, one has to experience code across the the entire spectrum of quality, from the very worst way to accomplish something, to the very best. Unfortunately, it can be difficult for begining programmers to do this, which is why I wrote an article that 

Usually a begining programmer is working by themselves, either through solo-coursework, or through self-taught delving into various projects. And, let's be honest, nobody started great at this, which means you're normally just exposed to your code, and it's not very good. This exposure to only bad code is further exacerbated by the fact that more collaborative endevours such as code review, working on opensource projects, or developing code for research applications is something beyond the skillset of a beginner. This means that the average novice coder only sees code that they've written, or which they've accessed through textbooks / forums such as StackOverflow. Now while both of these can be intimidating or downright hostile to newbies, I think the bigger detriments come in how the answers are couched, which makes it difficult to see the quality or understand the design decisions. Some common issues as I see them are that 1) only one answer to a problem is provided (which doesn't show a spectrum of answers and makes coding seem like any answer outside of this is invalid), 2) the reasoning behind the coding decisions is left out(this is largely unintentional, it just takes a lot of time to explain. Still, this is useful context if you are below  the skill-level of the answer-writer), or 3) when there *are* multiple answers, it can be difficult to determine which answer is better than which and why. 

Because of this, I've decided to put together a case-study to help coders that are just entering into the art of refactoring understand how to go about writing better code. To do this,  I present a problem and my solution, and then show several potential alternate solutions in order of least to most effective. By including a full spectrum in order, eith rationale, and critiques, my hope is that the reader can take away some key points about how to write better code. 


# The Problem

The following is a solution to https://www.hackerrank.com/challenges/mini-max-sum/problem, in which a Python script must return the minimum and maximum possible values that can be created by summing the values of a list after removing any one element. This must also be done as quickly as possible, which means that the solution must account for scaling.  A full summary of the problem (and an example answer) can be found below.

![alt text](https://github.com/Fehiroh/hackerrank_problem_solving_MinMaxSum/blob/master/mini-max-sum-English.jpg "The Problem Statement")

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
    min_val, max_val = arr[0]
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

In order to explain *why* this code is a great solution,  I've written some alternate snippets of code that solve the problem in several less efficient ways. I've included them below, and will go through how their logic works, and how they compare to the original solution. They are arranged according to efficiency, with the least efficient at the top and the most efficient at the bottom. 


### Calculating Every Possible Sum 

An easy mistake to make in coding, especially when you're new, is to take the problem statement at face-value. If we want the highest and lowest sums possible  after removing one element, I should calulate the sum of each possible solution, and keep the highest and lowest results. 

In order to accomplish this, one would have to create initial `min_sum`s and `max_sum` by summing without any one given element, create every possible sum, and run comparisons to find the real `min_sum` and `max_sum`.  The code would look something like this: 

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


While understandable, this is a *terrible* way to go about solving this problem. Firstly, the code is longer and harder to read than the "optimal" solution, but it also requires every element to be run through a `sum()` function `len(arr)` times, and the entire array to be duplicated `len(arr)` times. When you are dealing with data structures that contain observations in the millions or billions, this function would take hours to run. It is particularily worth noting that  none of the other solutions require an `x.copy()`, whereas this solution does. As a result, a significant portion of run-time is 100% unnecessary if you successfully reframe the problem. In fact, this failure to reframe is what makes this solution somewhat unbelievable, since the implementation requires one to possess enough coding accumen they would likely fall into an easier trap, such as using `x.sort()`. This is the kind of code that emerges when people are capable of breaking down a problem, but rely much too heavily on pasting in code snippets from forums such as StackOverflow. There's nothing wrong with borrowing chunks when you start out or understand how/why the answers work, but it can lead to creating the worst possible solution. 

### Using an `x.sort()`

Those people that jumped for the `x.sort()` have gone ahead and broken down the problem a little further. They've realized that we don't actually need every possible sum. What we need is to subtract the lowest value and the highest values of the array/list from a sum of all original elements. This is an element of all further solutions, so it's quite astute. However, instead of trying to go directly for these through a `min()` and/or `max()`, they have reached a solution where they order everything before going for the minimum and maximum via indexing. It should look something like this:

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

This is a *much* better than the first alternate, but it is ultimately still extremely bad. The two reasons for this are that 1) a full sort is unnecessary, and 2) sorts don't scale well; regardless of sorting algorithm, any sort will require every element within a set to be compared against multiple elements. The absolute lowest number of checks would be one, but that's with a set that only has two elements. As you increase the length of `arr`, more and more comparisons are required, and the sort time will generally increases non-linearly. This can be a worthwhile trade-off if you do infact need the entire sorted list. However, since we would immediately discard everything except the min and max, it makes more sense to only ever compare against these values. 

### `Min()` and ` Max()`

The observation that we only really need the min and the max is the corner-stone of our next solution. Anyone who has included `min()` and `max()` into their solution truly understands the problem, whether or not they understand the underlying binary iteration that makes those functions run so quickly.  This code is clean, easy to read, and will return values exponentially faster than the previous solutions. I've included two versions of this solution, one is fewer lines, but harder to read quickly, while the other is more pythonic. Remember, while throwing a nice one-liner can be a big dopamine hit, writing longer/more-pythonic code with well-named variables means your work will be easier to read, share, expand, and maintain. OOP obviously comes into the discussion too, at this point, but I'm planning to cover that in another repo. Regardless, even if you are going for short code since you only care about one thing in the local scope, nobody is impressed by code that repeats itself while trying to look concis; the two-liner is a two-liner because it doesn't double up work by calculating the sum twice. 


#### Two-liner Min/Max
```python
# two-liner
def miniMaxSum(arr):
    init_sum = sum(arr)
    print(init_sum - max(arr), init_sum - min(arr))
```

#### Pythonic Min/Max
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

Overall, both of these solutions are easier to read, and scale linearly, which makes them exponentially better than the previous solutions. However, there is still some slight tweaking possible. The most obvious one (to me, at least) is that making use of `min()` and `max()` requires two iterations through `arr`. Let's return to the optimal solution to see how it reduces the amount of iterations to 1. 

### Returning to the Solution 

While understanding how `min()` and `max()` work wasn't necessary before, it is now. Each of these functions essential work as a for-if. By switching out the `min()` and `max()` for an if/elif, only one iteraction through arr is necessary. Instead of every element going through two binary conditionals, many will only go through one. Additionally, by starting the range within the for-loop at 1, we bypass an unnecessisary comparison of the first element to itself. This is largely unnecesary in this particular excercise, but will make the function ever so slightly better than someone who did not include this detail. 

```python
#   Solution 
def miniMaxSum(arr):
    init_sum = sum(arr)
    min_val, max_val = arr[0]
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

# Conclusion

Based on all these solutions, I hope you've come away with a few simple lessons about how to tackle coding problems and refactoring: 
    1. Understand your Problem (inputs, outputs)
    2. Determine the knowledge required to derive the output from your input. 
    3. Find the way to determine that knowledge by using:
        a) the smallest possible subset of the original input.
        b) the fewest comparisons 
        c) the fewest number of iteractions. 
    4. As always, document your code and strive for readability. 

