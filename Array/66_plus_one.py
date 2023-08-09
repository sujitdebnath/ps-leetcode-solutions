class Solution:
    def plusOne(self, digits):
        for ind in range(len(digits)-1, -1, -1):
            if ind == len(digits) - 1:
                sum = digits[ind] + 1
            else:
                sum = digits[ind] + carry
            
            digits[ind] = sum % 10
            carry       = sum // 10
        
        if carry != 0:
            digits.insert(0, carry)
        
        return digits


digits = [9,9,9,9]
sol    = Solution()
print(sol.plusOne(digits))