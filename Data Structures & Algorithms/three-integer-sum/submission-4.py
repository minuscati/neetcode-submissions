class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sort = sorted(nums)
        k = len(nums_sort)
        Ans = set()
        for i in range(k):
            left = i+1
            right = k-1
            while left<right:
                sum = nums_sort[left]+nums_sort[right]
                if sum+nums_sort[i]==0:
                    Ans.add((nums_sort[i],nums_sort[left],nums_sort[right]))
                    left +=1
                    right-=1
                elif sum+nums_sort[i]>0:
                    right-=1
                else:
                    left+=1
        Ans = [list(x) for x in Ans]
        return Ans