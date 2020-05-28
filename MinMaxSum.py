# -*- coding: utf-8 -*-
"""
Created on Thu May 28 12:33:22 2020

@author: User
"""


# solution to https://www.hackerrank.com/challenges/mini-max-sum/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    init_sum = sum(arr)
    min_val = arr[0]
    max_val = arr[0]
    for i in range(0, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
        elif arr[i] > max_val:
            max_val = arr[i]
    print(init_sum-max_val, init_sum-min_val)



if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
