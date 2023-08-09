class Solution:
    def lengthOfLastWord(self, s):
        len_last_word = 0
        first_char_flag = False
        ind = len(s) - 1

        while ind >= 0:
            if s[ind] == " " and first_char_flag:
                break
            elif s[ind] != " " and not first_char_flag:
                first_char_flag = True
                len_last_word  += 1
            elif s[ind] != " " and first_char_flag:
                len_last_word += 1
            ind -=1
        
        return len_last_word


s   = "   fly me   to   the moon  "
sol = Solution()
print(sol.lengthOfLastWord(s))