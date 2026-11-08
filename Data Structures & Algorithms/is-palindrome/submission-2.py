class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [e.lower() for e in s if e.isalnum()]
        s_r = s[::-1]
        return s == s_r