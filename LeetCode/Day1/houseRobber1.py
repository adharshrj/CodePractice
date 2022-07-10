# Given an array of numbers where each element represents the value of each house,
# find the maximum amount that can be robbed. Condition: Cannot rob both houses
# if two house are adjacent

def houserobber(profit):
    rob1, rob2 = 0, 0

    for p in profit:
        nextrob = max(rob1 + p, rob2)
        rob1 = rob2
        rob2 = nextrob
    return rob2

print(houserobber([2,7,9,11,15]))