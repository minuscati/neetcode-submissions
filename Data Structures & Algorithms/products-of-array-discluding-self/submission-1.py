class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    # need extra understanding
        # inefficient
        # Answer = []
        # for i in range(len(nums)):
        #     j = 0
        #     k = len(nums)-1
        #     p_l = 1
        #     p_r = 1
        #     while j<i:
        #         p_l=p_l*nums[j]
        #         j+=1
        #     while i<k:
        #         p_r=p_r*nums[k]
        #         k-=1
        #     Answer.append(p_l*p_r)
        # return Answer
        
        n = len(nums)
        Answer = [1] *n
        prefix = 1
        for i in range(n):
            Answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1,-1,-1):
            Answer[i] *= suffix
            suffix *= nums[i]

        return Answer
