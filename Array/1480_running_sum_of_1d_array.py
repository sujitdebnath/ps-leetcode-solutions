class Solution:
    def runningSum(self, nums):
        sum = 0
        output_arr = list()

        for num in nums:
            sum = sum + num
            output_arr.append(sum)
        
        return output_arr

input_arr = [3,1,2,10,1]
sol = Solution()
print(sol.runningSum(input_arr))