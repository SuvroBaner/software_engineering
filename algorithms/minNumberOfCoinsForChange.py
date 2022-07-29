class minNumberOfCoinsForChange:
    def __init__(self, n, denoms):
        self.n = n
        self.denoms = denoms

    # Time : O(n*d) where n is the amount and d is the denom
    # Space : O(n)
    def solution(self):
        num_coins = [float("inf") for amount in range(self.n + 1)]
        num_coins[0] = 0
        for denom in self.denoms:
            for amount in range(len(num_coins)):
                if denom <= amount:
                    num_coins[amount] = min(num_coins[amount], 1 + num_coins[amount - denom])
            
        return num_coins[n] if num_coins[n] != float("inf") else -1    

# -- Testing the solution -
n = 7
denoms = [1, 5, 10]
obj = minNumberOfCoinsForChange(n, denoms)
print(obj.solution())


