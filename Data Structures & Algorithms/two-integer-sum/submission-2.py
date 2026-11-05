class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen  = {}
        Answer = []
        for i,v in enumerate(nums):
            complement = target-v
            if complement in seen:
                Answer.append(seen[complement])
                Answer.append(i)
            else:
                seen[v] = i
        return Answer