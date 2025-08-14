class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(0, n-2):
            x = nums[i]
            if i > 0 and x == nums[i-1]:
                continue
            if x + nums[n-1] + nums[n-2] < 0: #优化一
                continue
            if nums[n-3] + nums[n-1] + nums[n-2] < 0: #优化二
                break
            j = i+1
            k = n-1
            while j < k:
                sum = x+nums[j] + nums[k]
                if sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
                elif sum == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:  # 跳过重复数字
                        j += 1
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:  # 跳过重复数字
                        k -= 1
        return ans