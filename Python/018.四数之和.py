class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 法1.递归到2sum O(n^3) and O(n)
        nums.sort()
        results = []
        self.findNsum(nums, target, 4, [], results)
        return results
    
    def findNsum(self, nums, target, N, result, results):
        if len(nums) < N or N <2:
            return
        
        if N == 2:
            l, r = 0, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums) - N + 1):
                if target < nums[i] * N or target > nums[-1] * N:
                    break
                if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                    self.findNsum(nums[i+1:], target - nums[i], N- 1, result + [nums[i]], results)
        return
                    
