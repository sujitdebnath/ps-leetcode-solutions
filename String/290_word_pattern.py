class Solution:
    def wordPattern(self, pattern, s):
        words = s.split()

        if len(pattern) != len(words):
            return False
        elif len(set(pattern)) != len(set(words)):
            return False

        pattern_dict = dict()
        for letter, word in zip(pattern, words):
            if (letter not in pattern_dict.keys() and
                word not in pattern_dict.values()):
                pattern_dict[letter] = word
            elif (letter not in pattern_dict.keys() and
                word in pattern_dict.values()):
                pattern_dict[letter] = None

        for ind, letter in enumerate(pattern):
            if pattern_dict[letter] != words[ind]:
                return False
        
        return True


sol = Solution()
print(sol.wordPattern("abba", "dog dog cat dog"))