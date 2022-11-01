from typing import List


class Solution:
    # Time : O(n) | Space : O(1)
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in reversed(range(len(nums) - 1)):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False

nums = [2, 3, 1, 1, 4]
nums = [3, 2, 1, 0, 4]
nums = [0, 1]
nums = [0]
sol = Solution()
print(sol.canJump(nums))