class Solution:
    def numberOfSteps(self, num):
        step_counter = 0
        
        while num > 0:
            if num%2 == 0:
                num /= 2
            else:
                num -= 1
            
            step_counter += 1
        
        return step_counter


num = 123
sol = Solution()
print(sol.numberOfSteps(num))