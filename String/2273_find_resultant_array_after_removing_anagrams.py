class Solution:
    def removeAnagrams(self, words):
        sorted_words = ["".join(sorted(word)) for word in words]

        first_word = sorted_words[0]
        dup_count  = 0
        
        for ind, second_word in enumerate(sorted_words[1:], start=1):
            if first_word == second_word:
                words.pop(ind-dup_count)
                dup_count += 1
            else:
                first_word = second_word
        
        return words


words = ["abba","baba","bbaa","cd","cd"]
sol   = Solution()
print(sol.removeAnagrams(words))