class Solution:
    def search(self, nums: List[int], target: int) -> int:
    # 不理解边界条件
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)//2

            if nums[mid]==target:
                return mid

            if nums[left]<=nums[mid]:#左半边有序

                if nums[left]<=target<nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:#右半边有序
                if nums[mid]<target<=nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1