class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        k = len(numbers)
        seen = {}
        for i in range(k):
            complement = target-numbers[i]
            if complement in seen.keys():
                return [seen[complement],i+1]
            else:
                seen[numbers[i]]=i+1