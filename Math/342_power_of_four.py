import math

class Solution:
    def isPowerOfFour(self, n):
        return n > 0 and round(math.log(n, 4), 10).is_integer()


num_dict = {
    -64: False, -16: False, -4: False, -1: False, 0: False,
    1: True, 4: True, 16: True, 64:True,
    5: False, 1023: False, 1024: True,
    1073741823: False, 1073741824: True, 4294967297: False, 4294967296: True
}

sol = Solution()
for num in num_dict.keys():
    cal_res = sol.isPowerOfFour(num)
    result = num_dict[num]

    if num <= 0:
        print("Log4({}) = {}, ({}, {})".format(num, "math error", cal_res, result), end= " ")
    else:
        print("Log4({}) = {}, ({}, {})".format(num, round(math.log(num, 4), 10), cal_res, result), end=" ")
    
    if cal_res != result:
        print("-> Mismatch!")
    else:
        print()