class Solution:
    def canConstruct(self, ransomNote, magazine):
        ransom_note_dict = self.countingChar(ransomNote)
        magazine_dict    = self.countingChar(magazine)
        
        for ch in ransom_note_dict.keys():
            if ch not in magazine_dict.keys() or ransom_note_dict[ch] > magazine_dict[ch]:
                return False
        
        return True
    
    def countingChar(self, str):
        counting_dict = dict()

        for ch in str:
            if ch not in counting_dict.keys():
                counting_dict[ch] = 1
            else:
                counting_dict[ch] = counting_dict[ch] + 1
        
        return counting_dict


ransomNote = "aaabcdegegg"
magazine   = "abcdbcaagggege"
sol        = Solution()
print(sol.canConstruct(ransomNote, magazine))