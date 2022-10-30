from typing import List


class Solution:
    # Time : O(n^2) | Space : O(n)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for i in range(len(nums) - 2):
            # To handle the duplicate for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            first = nums[i]
            leftIdx = i + 1
            rightIdx = len(nums) - 1
            while leftIdx < rightIdx:
                second = nums[leftIdx]
                third = nums[rightIdx]
                total_sum = first + second + third
                if total_sum < 0:
                    leftIdx += 1
                elif total_sum > 0:
                    rightIdx -= 1
                else:
                    results.append([first, second, third])
                    # to handle the subsequent duplicates for second and third numbers
                    while leftIdx < rightIdx and nums[leftIdx] == nums[leftIdx + 1]:
                        leftIdx += 1
                    while leftIdx < rightIdx and nums[rightIdx] == nums[rightIdx - 1]:
                        rightIdx -= 1
                    leftIdx += 1
                    rightIdx -= 1
        
        return results

nums = [-1, 0, 1, 2, -1, -4]
# nums = [0, 0, 0]
# nums = [0, 1, 1]
nums = [-2, 0, 0, 2, 2]
#nums = [-4, -1, -1, 0, 1, 1, 1, 2, 2, 2]
sol = Solution()
print(sol.threeSum(nums))