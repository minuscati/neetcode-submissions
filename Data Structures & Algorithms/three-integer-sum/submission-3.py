class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
# fix one number + HashMap
        nums = sorted(nums)
        Ans = set()
        for i in range(len(nums)):
            seen = set()

            for j in range(i+1,len(nums)):
                complement = -nums[i]-nums[j]
                if complement in seen:
                    Ans.add((nums[i],complement,nums[j]))
                else:
                    seen.add(nums[j])
        return [list(x) for x in Ans]