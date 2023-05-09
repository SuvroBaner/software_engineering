from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        curMin, curMax = 1, 1

        for num in nums:
            if num == 0:
                curMin, curMax = 1, 1
                continue

            temp = curMax
            curMax = max(num, curMax * num, curMin * num)
            curMin = min(num, temp * num, curMin * num)
            result = max(result, curMax)
        
        return result


sol = Solution()
nums = [2, 3, 4, 5]
nums = [2, 3, -2, 4]
nums = [-2, 0, -1]
nums = [-2, -3, -4, -5]
nums = [2, -3, -5, -6]
nums = [2, -5, -2, -4, 3]

print(sol.maxProduct(nums))