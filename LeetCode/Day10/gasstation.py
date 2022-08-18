# Given two arrays, gas and cost find the starting point from which we can come full circle.

def gasstation(gas, cost):
    if sum(gas) < sum(cost):
        return - 1
    
    total = start = 0
    for i in range(len(gas)):
        total += (gas[i] - cost[i])

        if total < 0:
            total = 0
            start = i + 1
        
    return start


gas = [1,2,3,4,5] 
cost = [3,4,5,1,2]

print(gasstation(gas, cost))