class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        l_ind = 0
        cnt = defaultdict(int)  
        # 维护从下标 left 到下标 right 的字符及其出现次数
        for r_ind, r_ch in enumerate(s):
            cnt[r_ch] += 1
            while cnt[r_ch] > 1:
                cnt[s[l_ind]] -= 1
                l_ind += 1
            
            ans = max(ans, r_ind - l_ind + 1)

        return ans
