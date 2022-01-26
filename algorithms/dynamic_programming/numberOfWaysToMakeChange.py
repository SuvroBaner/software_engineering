# Time : O(n * d) where n = the total amount, d = the denominations
# Space : O(n)

def numberOfWaysToMakeChange(n, denoms):
    waysArray = [0 for i in range(n+1)]
    waysArray[0] = 1
    
    for denom in denoms:
        for amount in range(1, len(waysArray)):
            if denom <= amount:
                waysArray[amount] += waysArray[amount - denom]
    return waysArray[-1]

n = 6
denoms = [1, 5]
print(numberOfWaysToMakeChange(n, denoms))

n = 10
denoms = [1, 5, 10, 25]
print(numberOfWaysToMakeChange(n, denoms))

n = 9
denoms = [10]
print(numberOfWaysToMakeChange(n, denoms))

n = 9
denoms = [5]
print(numberOfWaysToMakeChange(n, denoms))