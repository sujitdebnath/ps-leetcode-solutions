class Solution:
    def reverse(self, x):
        if x < 0:
            x           = abs(x)
            is_negative = True
        else:
            is_negative = False
        
        reverse_x = 0
        while x != 0:
            last_digit = x % 10
            reverse_x  = reverse_x * 10 + last_digit
            x          = x // 10
        
        if is_negative:
            reverse_x = -1 * reverse_x
        
        if -2**31 > reverse_x or reverse_x > (2**31 - 1):
            return 0
        else:
            return reverse_x


x   = 1234567891
sol = Solution()
print(sol.reverse(x))