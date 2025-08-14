class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0 or k == 1:
            return 0
        prod = 1
        ans = 0
        l_ind = 0
        for r_ind, r_val in enumerate(nums):
            prod *= r_val
            while prod >= k and l_ind < len(nums):
                prod /= nums[l_ind]
                l_ind +=1

            ans += r_ind - l_ind + 1
        
        return ans
            
                