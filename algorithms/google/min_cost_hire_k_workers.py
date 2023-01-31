from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        num_max_ratios = n - k + 1
        max_wage_ratios = [0] * n
        
        for i, (w, q) in enumerate(zip(wage, quality)):
            ratio = float(w / q)
            max_wage_ratios[i] = ratio
            
        max_wage_ratios = sorted(max_wage_ratios, reverse = True)[: num_max_ratios]
        
        min_paid_wage = float("inf")
        for r in max_wage_ratios:
            final_wages = [0] * n
            correct_wage = 0
            for i in range(len(quality)):
                w = r * quality[i]
                if w >= wage[i]:
                    final_wages[i] = w
                    correct_wage += 1
                else:
                    final_wages[i] = float("inf")
                    
            if correct_wage >= k:
                final_wages = sorted(final_wages)[:k] # all the pos inf will be removed here
                min_paid_wage = min(min_paid_wage, sum(final_wages))
                print(min_paid_wage, correct_wage, r)
            
        return min_paid_wage
             
    
sol = Solution()
quality = [10, 20, 5]
wage = [70, 50, 30]
k = 2

# quality = [3, 1, 10, 10, 1]
# wage = [4, 8, 2, 2, 7]
# k = 3


print(sol.mincostToHireWorkers(quality, wage, k))