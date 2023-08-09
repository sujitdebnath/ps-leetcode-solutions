class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False

        reserve_x = x
        reverse_x = 0
        while reserve_x > 0:
            rem = reserve_x % 10
            reverse_x = reverse_x * 10 + rem
            reserve_x = int(reserve_x / 10)
        
        if reverse_x == x:
            return True
        else:
            return False



x = [121, -121, 10]
sol = Solution()
for num in x:
    print(num, sol.isPalindrome(num))