from typing import List

class Solution:
    # Time : O(n) where 'n' is the length of the seats array
    # Space : O(1)
    def maxDistToClosest(self, seats: List[int]) -> int:
        first_one = len(seats)
        last_one = -1
        max_dist = float("-inf")
        for idx in range(len(seats)):
            if seats[idx] == 0:
                i = idx - 1
                left_dist = 1
                while i >= 0 and seats[i] != 1:
                    left_dist += 1
                    i -= 1
                
                j = idx + 1
                right_dist = 1
                while j < len(seats) and seats[j] != 1:
                    right_dist += 1
                    j += 1
            
                closest_dist = min(left_dist, right_dist)
                max_dist = max(max_dist, closest_dist)
            else:
                first_one = min(first_one, idx)
                last_one = max(last_one, idx)
        
        # edge case if the 1st or/and last index has 0
        if seats[0] == 0:
            dist = first_one - 0
            max_dist = max(max_dist, dist)
        if seats[-1] == 0:
            dist = len(seats) - 1 - last_one
            max_dist = max(max_dist, dist)

        return max_dist

seats = [1, 0, 0, 0, 1, 0, 1]
seats = [1, 0, 0, 0]
seats = [0, 0, 0, 0, 1]
sol = Solution()
print(sol.maxDistToClosest(seats))