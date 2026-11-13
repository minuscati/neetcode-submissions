class Solution:
        def search(self, nums: List[int], target: int) -> int:
        # 不要改变原数组 而是移动指针
            left = 0
            right= len(nums)-1

            while left <= right:
                mid = (left+right)//2

                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right=mid-1
                elif nums[mid] < target:
                    left = mid+1
            return -1

#左闭右闭：明确mid前后，减少搜索范围+避免死循环