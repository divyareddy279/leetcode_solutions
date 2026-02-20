from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        return self.res(0, nums, dp)
    
    def res(self, i, nums, dp):
        if i >= len(nums):
            return 0
        
        if dp[i] != -1:
            return dp[i]
        
        take = nums[i] + self.res(i + 2, nums, dp)
        not_take = self.res(i + 1, nums, dp)
        
        dp[i] = max(take, not_take)
        return dp[i]