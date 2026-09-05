class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f_of_s = {}
        f_of_t = {}
        
        for char in s:
            if char in f_of_s:
                f_of_s[char] += 1
            else:
                f_of_s[char] = 1
                
        for char in t:
            if char in f_of_t:
                f_of_t[char] += 1
            else:
                f_of_t[char] = 1
                
        if f_of_s == f_of_t:
            return True
        else:
            return False