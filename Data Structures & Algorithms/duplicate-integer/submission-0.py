class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}

        for i in nums:
            if i in count: #i作为count的键不是第一次出现
                return True
            else:#i第一次作为count的键出现
                count[i] =1
        return False
