class Solution:
    def isPalindrome(self, s: str) -> bool:
    # 思路：小写所有词->正反遍历->判断相同
        s_n = []
        s_r = [] 
        for e in s:
            if e.isalnum()==True:
                s_n.append(e.lower())
        # s_n = s_n.lower()
        for i in range(len(s_n)-1,-1,-1):
            s_r.append(s_n[i])
        if s_n == s_r:
            return True
        else:
            return False