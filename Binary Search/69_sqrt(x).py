class Solution:
    def mySqrt(self, x):
        max_perfect_sqr = 0

        while max_perfect_sqr*max_perfect_sqr <= x:
            max_perfect_sqr = max_perfect_sqr + 1
        
        return max_perfect_sqr - 1


x_list = [0,1,2,3,4,5,6,7,8,9,10,14,15,25,30,36,40,49,56,120,121,400,500,1073741824,2147483646,2147483647]
sol = Solution()
for x in x_list:
    print(f"sqrt({x}) = {sol.mySqrt(x)}")