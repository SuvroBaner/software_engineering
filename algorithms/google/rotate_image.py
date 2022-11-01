from typing import List

class Solution:
    # Time : O(n^2) | Space : O(1)
    def rotate(self, matrix: List[List[int]]) -> None:
        left = 0
        right = len(matrix) - 1
        while left < right:
            for i in range(right - left): # there is always an n-1 rotations.
                # we can define the top and bottom here as it is a square matrix
                top = left
                bottom = right
            
                top_left = matrix[top][left + i] 

                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = top_left
            
            left += 1
            right -= 1
        return matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
sol = Solution()
print(sol.rotate(matrix))