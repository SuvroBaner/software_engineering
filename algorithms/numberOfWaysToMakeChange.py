class numberOfWaysToMakeChange:
    def __init__(self, n, denoms):
        self.n = n
        self.denoms = denoms

    # Time : O(n*d) where n is the amount and d is the number of denoms
    # Space : O(n)
    def solution(self):
        ways = [0] * (self.n + 1)
        ways[0] = 1
        
        for denom in self.denoms:
            for amount in range(1, len(ways)):
                if amount < denom:
                    continue
                ways[amount] = ways[amount] + ways[amount - denom]
        return ways[-1]

# --- Testing the solution 
n = 6
denoms = [1, 5]
n = 10
denoms = [1, 5, 10, 25]
obj = numberOfWaysToMakeChange(n, denoms)
print(obj.solution())