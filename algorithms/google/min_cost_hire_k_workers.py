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
                total_wage = min(total_wage, self.findSumOfKSmallest(paid_wage, k))
                print('Worker: {} rate'.format(i), paid_wage)
                print('Minimum total paid wage ', total_wage)
                print("\n")
      
        return total_wage
    
    def findSumOfKSmallest(self, wages, k):
        wages.sort()
        return sum(wages[0:k])
    
sol = Solution()
quality = [10, 20, 5]
wage = [70, 50, 30]
k = 2

quality = [3, 1, 10, 10, 1]
wage = [4, 8, 2, 2, 7]
k = 3

print(sol.mincostToHireWorkers(quality, wage, k))
                
                