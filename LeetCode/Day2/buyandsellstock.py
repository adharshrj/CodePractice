# Given an array of stock prices on each day of a week, calculate the maximum profit that can be made by buying and selling the stock
# right pointer is < len(input) is the condition for loop

def buyandsellstock(prices):
    maxprofit = 0
    l, r = 0, 1

    while r < len(prices):
        if prices[r] > prices[l]:
            profit = prices[r] - prices[l]
            maxprofit = max(maxprofit, profit)
        else:
            l = r
        r += 1
    
    return maxprofit

print(buyandsellstock([7,1,5,3,6,4]))