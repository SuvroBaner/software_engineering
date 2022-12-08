from typing import List

class Solution:
    # def trap(self, height: List[int]) -> int:
    #     peaks = []
    #     for i in range(1, len(height) - 1):
    #         if height[i] > height[i - 1] and height[i] > height[i + 1]:
    #             peaks.append(i)

    #     total = 0
    #     not_found = False
    #     for i, peak_idx in enumerate(peaks):
    #         right_idx = peak_idx + 1
    #         count = 0
    #         blocks = 0
    #         while right_idx < len(height) - 1 and height[right_idx] < height[peak_idx]:
    #             count += 1
    #             blocks += height[right_idx]
    #             right_idx += 1
            
    #         if i < len(peaks) - 1 and right_idx >= len(height) - 1:
    #             count = 0
    #             blocks = 0
            
    #         if not_found:
    #             left_idx = peak_idx - 1
    #             while left_idx >= 0 and height[left_idx] < height[peak_idx]:
    #                 count += 1
    #                 blocks += height[left_idx]
    #                 left_idx -= 1
            
    #         total += (height[peak_idx] * count) - blocks

    #         if i < len(peaks) - 1 and right_idx >= len(height) - 1:
    #             not_found = True 

    #     return total

    # Time : O(n) | Space : O(n)
    # def trap(self, height : List[int]) -> int:
    #     left_max = [0] * len(height)
    #     right_max = [0] * len(height)

    #     maximum = 0
    #     for i in range(len(height)):
    #         if height[i] > maximum:
    #             left_max[i] = height[i]
    #             maximum = height[i]
    #         else:
    #             left_max[i] = maximum
        
    #     maximum = 0
    #     for i in reversed(range(len(height))):
    #         if height[i] > maximum:
    #             right_max[i] = height[i]
    #             maximum = height[i]
    #         else:
    #             right_max[i] = maximum

    #     total = 0
    #     for i in range(1, len(height) - 1):
    #         total += round(min(left_max[i], right_max[i]) - height[i])
        
    #     return total
    
    # Time : O(n) | Space : O(1)
    def trap(self, height : List[int]) -> int:
        if not height:
            return 0
        
        leftIdx = 0
        rightIdx = len(height) - 1
        left_max = height[leftIdx]
        right_max = height[rightIdx]
        total = 0

        while leftIdx < rightIdx:
            if left_max < right_max:
                leftIdx += 1
                left_max = max(left_max, height[leftIdx])
                total += left_max - height[leftIdx]
            else:
                rightIdx -= 1
                right_max = max(right_max, height[rightIdx])
                total += right_max - height[rightIdx]
        return total

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
#height = [4, 2, 0, 3, 2, 5]
sol = Solution()
print(sol.trap(height))
