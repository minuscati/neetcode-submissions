class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_l = [e.lower() for e in s if e.isalnum()] 
        left = 0
        right = len(s_l)-1
        while left<right:
            if s_l[left] == s_l[right]:
                left +=1
                right-=1
            else:
                return False
        return True

