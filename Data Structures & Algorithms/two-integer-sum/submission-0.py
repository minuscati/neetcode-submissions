class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        answer_list = []
        for index, value in enumerate(nums):
            complement = target-value

            if complement in seen:
                answer_list.append(seen[complement])
                answer_list.append(index)
            else:
                seen[value]= index
        return answer_list
