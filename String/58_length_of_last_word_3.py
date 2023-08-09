class Solution:
    def lengthOfLastWord(self, s):
        len_last_word = 0
        s             = s.rstrip()
        ind           = len(s) - 1

        while ind >= 0 and s[ind] != " ":
            len_last_word += 1
            ind -=1
        
        return len_last_word


s   = "   fly me   to   the moon  "
sol = Solution()
print(sol.lengthOfLastWord(s))