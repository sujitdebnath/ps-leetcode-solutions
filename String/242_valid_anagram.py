class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        str_char_list = list(s)

        for char in t:
            if char not in str_char_list:
                return False
            str_char_list.remove(char)
        
        return True


s, t = "abaacde", "aabca"
sol = Solution()
print(sol.isAnagram(s, t))