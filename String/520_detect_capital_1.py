class Solution:
    def detectCapitalUse(self, word):
        if self.find_all_capitals(word):
            return True
        elif self.find_all_not_capitals(word):
            return True
        elif self.find_first_letter_captial(word):
            return True
        else:
            return False

    def find_all_capitals(self, word):
        for letter in word:
            if not letter.isupper():
                return False
        
        return True
    
    def find_all_not_capitals(self, word):
        for letter in word:
            if not letter.islower():
                return False
        
        return True
    
    def find_first_letter_captial(self, word):
        if word[0].isupper() and self.find_all_not_capitals(word[1:]):
            return True
        
        return False


sol = Solution()
print(sol.detectCapitalUse("FlaG"))