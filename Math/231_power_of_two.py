import math

class Solution:
    def isPowerOfTwo(self, n):
        return n > 0 and round(math.log2(n), 10).is_integer()


num_dict = {
    -32: False, -16: False, -2: False, -1: False, 0: False,
    1: True, 2: True, 4: True, 16:True,
    1023: False, 1024: True, 4096: True,
    33554431: False, 33554432: True, 1073741823: False, 1073741824: True,
    2147483648: True
}

sol = Solution()
for num in num_dict.keys():
    cal_res = sol.isPowerOfTwo(num)
    result = num_dict[num]

    if num <= 0:
        print("Log3({}) = {}, ({}, {})".format(num, "math error", cal_res, result), end= " ")
    else:
        print("Log3({}) = {}, ({}, {})".format(num, round(math.log2(num), 10), cal_res, result), end=" ")
    
    if cal_res != result:
        print("-> Mismatch!")
    else:
        print()