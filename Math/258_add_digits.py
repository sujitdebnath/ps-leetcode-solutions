class Solution:
    def addDigits(self, num):
        while num // 10 != 0:
            num = self.sumDigits(num)
        
        return num

    def sumDigits(self, num):
        sum = 0

        while num != 0:
            sum += num % 10
            num = num // 10
        
        return sum


sol = Solution()
print(sol.addDigits(0))