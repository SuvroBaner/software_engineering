from typing import List


class Solution:
    # Time : O(n) | Space : O(1)
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        digits.insert(0, 1)
        return digits

sol = Solution()
digits = [1, 2, 3]
digits = [9, 9, 9]
digits = [9, 8, 9]
digits = [9, 9, 1, 2, 3, 4, 5, 6, 8, 8, 9]
print(sol.plusOne(digits))