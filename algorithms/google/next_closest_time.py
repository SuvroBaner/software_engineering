class Solution:
    # Time : O(1) | Space : O(1)
    def nextClosestTime(self, time: str) -> str:
        hour, minute = time.split(":")

        # generate all possible 2 digit values
        nums = sorted(set(hour + minute))
        two_digit_values = []
        for one in nums:
            for two in nums:
                two_digit_values.append(one + two)
        
        mnt_idx = two_digit_values.index(minute)
        if mnt_idx + 1 < len(two_digit_values) and two_digit_values[mnt_idx + 1] < "60":
            return hour + ':' + two_digit_values[mnt_idx + 1]

        hr_idx = two_digit_values.index(hour)
        if hr_idx + 1 < len(two_digit_values) and two_digit_values[hr_idx + 1] < "24":
            return two_digit_values[hr_idx + 1] + ':' + two_digit_values[0]

        return two_digit_values[0] + ':' + two_digit_values[0]     

time = "19:34"
# time = "19:39"
# time = "16:36"
# time = "23:59"
# time = "01:34"
# time = "20:48"
sol = Solution()
print(sol.nextClosestTime(time))