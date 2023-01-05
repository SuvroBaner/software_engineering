from typing import List

class Solution:
    # Time : O(n*k) | Space : O(k)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = [float("-inf")] * k
        for i in range(len(nums)):
            num = nums[i]
            for j in range(len(res)):
                if num > res[j] and num > res[k-1]:
                    temp = res[j]
                    res[j] = num
                    num = temp
        return res[k-1]

sol = Solution()
nums = [3, 2, 1, 5, 6, 4]
k = 2
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(sol.findKthLargest(nums, k))
