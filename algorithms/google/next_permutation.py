from typing import List


class Solution:
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
    
    def reverse(self, nums, start, end):
        while start < end:
            self.swap(nums, start, end)
            start += 1
            end -= 1
    # Time : O(n) | Space : O(1)
    def nextPermutation(self, nums: List[int]) -> None:
        # if it is just one number, don't do anything
        if len(nums) == 1:
            return
        # if it is two numbers, do a swap
        if len(nums) == 2:
            return self.swap(nums, 0, 1)

        # if it is longer than two lets start from the end of the array and 
        # decrement to find which pair is not in order (right should be more than left)
        dec = len(nums) - 2
        while dec >= 0 and nums[dec] >= nums[dec + 1]:
            dec -= 1
        # so after "dec" every thing needs to be reversed to get the smallest number.
        self.reverse(nums, dec + 1, len(nums) - 1)
        # if the entire array is decremented then we now have the smallest number.
        # which is the solution
        if dec == - 1:
            return
        # otherwise we will swap the number at "dec" position with the number beyond which is the largest
        # that will give us the next permutation
        next_num = dec + 1
        while next_num < len(nums) and nums[next_num] <= nums[dec]:
            next_num += 1
        self.swap(nums, dec, next_num)


nums = [1, 2, 7, 9, 6, 4, 1]
#nums = [1, 2]
sol = Solution()
print(sol.nextPermutation(nums))