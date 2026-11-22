class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # find the meeting point
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # phase 2: find the entrance of the cycle
        # Floyd环检测算法
        slow2 = 0
        while slow!=slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow