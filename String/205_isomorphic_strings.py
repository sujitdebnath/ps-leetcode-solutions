class Solution:
    def isIsomorphic(self, s, t):
        char_mapping = self.charMapping(s, t)
        if char_mapping == None:
            return False

        str_t = ""
        for char_s in s:
            str_t = str_t + char_mapping[char_s]

        if t == str_t:
            return True
        else:
            return False
    
    def charMapping(self, s, t):
        char_mapping = dict()
        mapping_flag = False

        for char_s, char_t in zip(s, t):
            if char_s in char_mapping.keys():
                existing_char = char_mapping[char_s]
                if existing_char != char_t:
                    mapping_flag = True
                    break
            elif char_t in char_mapping.values():
                mapping_flag = True
                break
            else:
                char_mapping[char_s] = char_t
        
        if mapping_flag:
            return None
        else:
            return char_mapping


s = ["badc", "egg", "foo", "paper"]
t = ["baba", "add", "bar", "title"]
sol  = Solution()
for str_s, str_t in zip(s, t):
    print(sol.isIsomorphic(str_s, str_t))