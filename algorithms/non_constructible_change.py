class NonConstructibleChange:

    def __init__(self, coins):
        self.coins = coins

    # Time : O(nlogn) | Space : O(1)
    def solution1(self):
        self.coins.sort()
        currentTotalChange = 0
        for coin in self.coins:
            if coin > currentTotalChange + 1:
                return currentTotalChange + 1
            currentTotalChange += coin
        
        return currentTotalChange + 1

# Testing the result -

coins = []
coins = [1, 2, 3]
coins = [1, 2, 5]
coins = [5, 7, 1, 1, 2, 3, 22]
coins = [1, 1, 1, 1, 1]

obj = NonConstructibleChange(coins)
print(obj.solution1())
