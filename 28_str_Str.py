class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        flag = False
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                flag = True
                for j in range(len(needle)):
                    try:
                        if haystack[i + j] != needle[j]:
                            flag = False
                            break
                    except IndexError:
                        return -1
            if flag:
                return i
        
        return -1