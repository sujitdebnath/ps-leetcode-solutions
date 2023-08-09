class Solution:
    def mySqrt(self, x):
        low = 0
        high = x
        
        while low <= high:
            mid = (low+high) // 2

            if mid*mid < x:
                low = mid + 1
            elif mid*mid > x:
                high = mid - 1
            else:
                return mid
        
        return high


x_list = [0,1,2,3,4,5,6,7,8,9,10,14,15,25,30,36,40,49,56,120,121,400,500,1073741824,2147483646,2147483647]
sol = Solution()
for x in x_list:
    print(f"sqrt({x}) = {sol.mySqrt(x)}")