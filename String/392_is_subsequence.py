from queue import Queue

class Solution:
    def isSubsequence(self, s, t):
        queue_s = Queue(maxsize = len(s))
        queue_t = Queue(maxsize = len(t))

        for char_s in s:
            queue_s.put(char_s)

        for char_t in t:
            queue_t.put(char_t)
        
        while not queue_s.empty():
            char_s = queue_s.get()

            if queue_t.empty():
                return False
            else:
                while not queue_t.empty():
                    char_t = queue_t.get()
                    if char_s == char_t:
                        break
                    elif queue_t.empty():
                        return False

        return True


s = ["abc", "axc", "aaaaaa", "aaaa"]
t = ["ahbgdc", "ahbgdc", "bbaaaa", "bbaaaa"]
sol  = Solution()
for str_s, str_t in zip(s, t):
    print(str_s, str_t, sol.isSubsequence(str_s, str_t))