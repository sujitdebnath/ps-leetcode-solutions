import math

class Solution:
    def isPowerOfThree(self, n):
        return n > 0 and round(math.log(n, 3), 10).is_integer()


num_dict = {
    -27: False, -9: False, -3: False, -1: False, 0: False,
    1: True, 3: True, 9: True, 27:True,
    240: False, 243: True, 19682: False,
    1162261466: False, 1162261467: True, 3486784400: False, 3486784401: True,
    12157665459056928801: True
}

sol = Solution()
for num in num_dict.keys():
    cal_res = sol.isPowerOfThree(num)
    result = num_dict[num]

    if num <= 0:
        print("Log3({}) = {}, ({}, {})".format(num, "math error", cal_res, result), end= " ")
    else:
        print("Log3({}) = {}, ({}, {})".format(num, round(math.log(num, 3), 10), cal_res, result), end=" ")
    
    if cal_res != result:
        print("-> Mismatch!")
    else:
        print()