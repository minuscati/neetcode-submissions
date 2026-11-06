class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        else:
            sorted_num = sorted(set(nums))
            continous_c = 1
            max_c = 1
            for i in range(1,len(sorted_num)):
                if sorted_num[i]-sorted_num[i-1]==1:
                    continous_c+=1
                else:
                    max_c = max(max_c,continous_c)
                    continous_c = 1
            max_c = max(max_c, continous_c)
            return max_c
                

