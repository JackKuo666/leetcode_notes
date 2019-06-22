class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 法1.dp最简版
        # def rob(nums):
        #     now = prev = 0
        #     for n in nums:
        #         now, prev = max(now, prev + n), now
        #     return now
        # return max(rob(nums[len(nums) != 1:]), rob(nums[:-1]))
        
        # 法2.dp易理解版
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        N = len(nums)
        return max(self.rob_range(nums[0 : N - 1]), self.rob_range(nums[1 : N]))
    
    def rob_range(self, nums):
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        N = len(nums)
        dp = [0] * N
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, N):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]

