from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        num_of_workers = len(wage)
        total_wage = float("inf")
        for i in range(num_of_workers):
            wage_per_quality = wage[i] / quality[i]
            paid_wage = []
            for j in range(num_of_workers):
                my_wage = quality[j] * wage_per_quality
                if my_wage >= wage[j]:
                    paid_wage.append(my_wage)
            if len(paid_wage) >= k:
                total_wage = min(total_wage, self.findSumOfKSmallest(paid_wage, k, do_sort = False))
                print('Worker: {} rate'.format(i), paid_wage)
                print('Minimum total paid wage ', total_wage)
                print("\n")
      
        return total_wage
    
    def findSumOfKSmallest(self, wages, k, do_sort):
        if len(wages) == k:
            return sum(wages)
        if do_sort:
            wages.sort()
            return sum(wages[0:k])
        
        return sum(self.quickSelect(wages, k))
    
    def quickSelect(self, nums: List[float], k: int) -> List[float]:
        old_k = k
        k = len(nums) - k
    
        def quickSelectHelper(l, r):
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            
            if p > k:
                return quickSelectHelper(l, p - 1) # left side of k
            elif p < k:
                return quickSelectHelper(p + 1, r) # right side of k
            else:
                return nums[:old_k]
            
        return quickSelectHelper(0, len(nums) - 1)    
    
sol = Solution()
quality = [10, 20, 5]
wage = [70, 50, 30]
k = 2

# quality = [3, 1, 10, 10, 1]
# wage = [4, 8, 2, 2, 7]
# k = 3

print(sol.mincostToHireWorkers(quality, wage, k))
                
                