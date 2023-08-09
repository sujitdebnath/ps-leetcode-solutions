class Solution:
    def concatenatedBinary(self, n):
        decimal_output = 0
        num_of_digit   = 0

        for decimal_num in range(n, 0, -1):
            bin_str = bin(decimal_num)[2:]

            for digit in bin_str[::-1]:
                if digit == "1":
                    decimal_output = (decimal_output + 2**num_of_digit) % (10**9 + 7)        
                num_of_digit += 1
        
        return decimal_output


n   = 3
sol = Solution()
print(sol.concatenatedBinary(n))