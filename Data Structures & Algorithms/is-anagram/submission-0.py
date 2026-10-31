class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Count_s = {}
        Count_t = {}
        for i in s:
            if i in Count_s:
                Count_s[i] += 1
            else:
                Count_s[i] = 1
        
        for j in t:
            if j in Count_t:
                Count_t[j] += 1
            else:
                Count_t[j] = 1
        
        if Count_s == Count_t:
            return True
        else:
            return False
