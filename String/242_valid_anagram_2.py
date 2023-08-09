class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        for char_s, char_t in zip(sorted(s), sorted(t)):
            if char_s != char_t:
                return False
        
        return True


s, t = "abaac", "aabca"
sol = Solution()
print(sol.isAnagram(s, t))