from typing import List


class Solution:
    # Time : O(n) | Space : O(1)
    def maxArea(self, height: List[int]) -> int:
        leftIdx = 0
        rightIdx = len(height) - 1
        max_area = 0
        while leftIdx < rightIdx:
            area = (rightIdx - leftIdx) * min(height[leftIdx], height[rightIdx])
            max_area = max(max_area, area)
            if height[leftIdx] <= height[rightIdx]:
                leftIdx += 1
            else:
                rightIdx -= 1
        return max_area

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
height = [1, 1]
height = [9, 7, 6, 4, 2]
height = [1, 2]
height = [2, 0]
sol = Solution()
print(sol.maxArea(height))