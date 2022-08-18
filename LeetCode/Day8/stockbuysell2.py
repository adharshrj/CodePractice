# Problem Description

# Say you have an array, A, for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit.

# You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

# However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

# Input Format:

# The first and the only argument is an array of integer, A.

# Output Format:

# Return an integer, representing the maximum possible profit.

def maxProfit(arr):
    cp = 0
    mxp = 0
    for i in range(len(arr)):
        cp = arr[i] - arr[0]
        arr[0] = arr[i]
        mxp += cp if cp > 0 else 0
    
    return mxp