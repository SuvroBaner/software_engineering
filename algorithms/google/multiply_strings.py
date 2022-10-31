class Solution:
    # Time : O(num1 * num2) | Space : O(num1 + num2)
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        result = [0] * (len(num1) + len(num2))
        # num1 : '123'
        # num2 : '456'
        num1, num2 = num1[::-1], num2[::-1]
        # num1 : '321'
        # num2 : '654'
        # we reverse so that we can loop from index 0
        for idx1 in range(len(num1)):
            for idx2 in range(len(num2)):
                digit = int(num1[idx1]) * int(num2[idx2])
                result[idx1 + idx2] += digit
                result[idx1 + idx2 + 1] += result[idx1 + idx2] // 10 # the carry
                result[idx1 + idx2] = result[idx1 + idx2] % 10
        
        # result = [8,8,0,6,5,0] # there is a leading zero which is trailing now as it has been reversed
        result = result[::-1] # reversing it back
        # result : [0,5,6,0,8,8]

        # handling the leading zero now-
        start = 0
        while start < len(result) and result[start] == 0:
            start += 1
        # result : [0, 5, 6, 0, 8, 8] and start = 1
        # Converting it to a string and joining them together
        result = map(str, result[start:])
        # result : ['5', '6', '0', '8', '8']
        return ''.join(result)
        # result : '56088'  

num1 = "2"
num2 = "3"
num1 = "10"
num2 = "10"
num1 = "123"
num2 = "456"
sol = Solution()
print(sol.multiply(num1, num2))