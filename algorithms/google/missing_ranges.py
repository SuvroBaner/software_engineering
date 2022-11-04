from time import time
from typing import List
from unittest import result
# class Solution:
#     def createString(self, s, e):
#         if s == e:
#             return str(s)
#         else:
#             return str(s) + "->" + str(e)
    
#     # Time : O(upper)
#     def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
#         if not nums:
#             return [self.createString(lower, upper)]
        
#         num_idx = max(0, lower) # this will interate over the nums array, it should atleast start from 0
#         start_idx = lower # this will be the start_idx for the missing interval
#         result = [] # this will store the missing intervals
#         for i in range(lower, upper + 1, 1):
#             # iterate over the entire range [lower, upper]
            
#             # to avoid out of bounds for nums array so it is restricted by num_idx
#             if num_idx > len(nums) - 1:
#                 break
            
#             num = nums[num_idx]
            
#             # This will be executed post there is a missing range and then they start appearing again
#             # we will keep the start_idx fixed since there happens a mismatch.
#             # so, that we get a missing range w.r.t "i"
#             # Consider this step to store the result and immediately the next if will run to set the values. 
#             if num == i and start_idx < i:
#                 result.append(self.createString(start_idx, i - 1))

#             # Good case, when there is no missing ranges, increment the num_idx so that in next iteraction
#             # the next nums value is processed.
#             # also keep start_idx equals to "i" before the next iteraion start
#             if num == i:
#                 start_idx = i + 1
#                 num_idx += 1
#             else:
#                 # when there is a mismatch, fix start_idx to get the start index of the missing range
#                 start_idx = min(start_idx, i)
        
#         if nums[num_idx - 1] == i:
#             # if the nums array ended with the "i" iteration
#             # in this case we have stored all the missing ranges already in the result list
#             return result
#         else:
#             # if nums array breaks out of the loop, we pick the last num add a 1 to get the lower bound of the missing range
#             # the upper bound in thd "upper", we add this to the result and return
#             return result +  [self.createString(nums[num_idx - 1] + 1, upper)]

class Solution:
    def createString(self, s, e):
        if s == e:
            return str(s)
        else:
            return str(s) + "->" + str(e)

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if not nums:
            return [self.createString(lower, upper)]
        
        if lower < nums[0]:
            nums.insert(0, lower - 1) # as lower bound is included
        if upper > nums[-1]:
            nums.append(upper + 1) # as upper bound is included

        diff_nums = [0] * (len(nums) - 1)

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            diff_nums[i - 1] = diff

        result = []
        for i in range(len(diff_nums)):
            if diff_nums[i] == 1:
                continue
            start_num = nums[i] + 1
            end_num = nums[i] + diff_nums[i] - 1
            result.append(self.createString(start_num, end_num))
        return result
        


nums = [1, 2, 6]
lower = -1
upper = 10
# nums = [0, 1, 4, 6, 7, 8, 9, 10]
# nums = [0, 1, 4, 6, 7, 8]
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lower = 0
# upper = 10
# nums = [-1]
# lower = -1
# upper = -1
# nums = [0,1,3,50,75]
# lower = 0
# upper = 99
# nums = []
# lower = 1
# upper = 1
# nums = [-1]
# lower = -2
# upper = -1
# nums = [1000000000]
# lower = 0
# upper = 1000000000
import time
start = time.time()
sol = Solution()
print(sol.findMissingRanges(nums, lower, upper))
end = time.time()
print(end - start)