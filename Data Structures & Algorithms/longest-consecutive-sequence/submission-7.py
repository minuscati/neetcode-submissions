class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_num = sorted(set(nums))
        if not sorted_num: #null list
            return 0
        
        k = len(sorted_num)
        count=1
        c=1
        
        for j in range(1,k):
            if sorted_num[j]-sorted_num[j-1]==1:
                c+=1
            else:
                c=1
                                    
            count = max(count,c)
        return count


