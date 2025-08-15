class Solution(object):
    # lower_bound 返回最小的满足 nums[i] >= target 的下标 i
    def lower_bound(self, nums, target):
        left, right = 0, len(nums)-1 # 闭区间 [left, right]
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid+1

        return left

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = self.lower_bound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1,-1]

        end = self.lower_bound(nums, target+1) - 1
        return [start, end]