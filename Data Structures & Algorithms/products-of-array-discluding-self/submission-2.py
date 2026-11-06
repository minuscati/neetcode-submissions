class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
# idea: 除自己的乘积可以拆解为左乘积和右乘积的积
        product_l = [1] * len(nums)
        for i in range(1,len(nums)):
            product_l[i] = nums[i-1]*product_l[i-1]
        
        product_r = [1] * len(nums)
        for i in range(len(nums)-2,-1,-1):
            product_r[i] = nums[i+1]*product_r[i+1]

        # return [v for v in product_l*product_r]
        return [a*b for a,b in zip(product_l, product_r)]



        